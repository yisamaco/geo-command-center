from __future__ import annotations

from pathlib import Path
import shutil

import typer
from rich import print
from sqlalchemy import text

from .db import make_engine, run_sql_file

app = typer.Typer(help="GEO Command Center CLI")
knowledge_app = typer.Typer(help="Knowledge commands")
app.add_typer(knowledge_app, name="knowledge")

ROOT = Path(__file__).resolve().parents[3]
MIGRATION_FILE = ROOT / "supabase" / "migrations" / "202605170001_init_geo_command_center.sql"
SEED_FILE = ROOT / "supabase" / "seed.sql"


@app.command("init")
def init_db() -> None:
    """Initialize database schema."""
    run_sql_file(str(MIGRATION_FILE))
    print(f"[green]Initialized schema from[/green] {MIGRATION_FILE}")


@app.command("seed")
def seed_db() -> None:
    """Seed base data (LLM platforms)."""
    run_sql_file(str(SEED_FILE))
    print(f"[green]Seeded data from[/green] {SEED_FILE}")


@app.command("run")
def run_prompt(prompt: str, platform: str = "OpenAI", access_method: str = "api") -> None:
    """Create a manual GEO run placeholder record."""
    engine = make_engine()
    with engine.begin() as conn:
        platform_id = conn.execute(text("select id from llm_platforms where name=:name limit 1"), {"name": platform}).scalar()
        conn.execute(
            text(
                """
                insert into geo_runs (run_name, prompt, llm_platform_id, access_method, run_mode, language, region)
                values (:run_name, :prompt, :llm_platform_id, :access_method, 'manual_geo', 'en', 'global')
                """
            ),
            {
                "run_name": f"CLI run - {platform}",
                "prompt": prompt,
                "llm_platform_id": platform_id,
                "access_method": access_method,
            },
        )
    print("[green]Inserted GEO run placeholder.[/green]")


@app.command("score")
def score_latest(scope: str = "api_geo") -> None:
    """Score latest run with mock MVP scores."""
    engine = make_engine()
    with engine.begin() as conn:
        latest_id = conn.execute(text("select id from geo_runs order by created_at desc limit 1")).scalar()
        if not latest_id:
            raise typer.BadParameter("No geo_runs records found. Run `geo run` first.")
        conn.execute(
            text(
                """
                insert into geo_scores (
                    geo_run_id, score_scope, brand_mention_score, position_score,
                    citation_accuracy_score, sentiment_score, competitor_dominance_score
                ) values (:geo_run_id, :score_scope, 70, 72, 68, 75, 60)
                """
            ),
            {"geo_run_id": latest_id, "score_scope": scope},
        )
    print(f"[green]Scored latest run with scope[/green] {scope}")


@knowledge_app.command("export")
def knowledge_export(slug: str, export_type: str = "markdown") -> None:
    """Export one knowledge entity into knowledge_exports."""
    engine = make_engine()
    with engine.begin() as conn:
        entity = conn.execute(
            text("select id, name, short_definition from knowledge_entities where slug=:slug limit 1"),
            {"slug": slug},
        ).mappings().first()
        if not entity:
            raise typer.BadParameter(f"Entity slug not found: {slug}")

        content = f"# {entity['name']}\n\n{entity['short_definition'] or ''}" if export_type == "markdown" else "{}"
        conn.execute(
            text(
                "insert into knowledge_exports (entity_id, export_type, content) values (:entity_id, :export_type, :content)"
            ),
            {"entity_id": entity["id"], "export_type": export_type, "content": content},
        )
    print(f"[green]Exported entity[/green] {slug} as {export_type}")


@app.command("report")
def generate_report(report_name: str = "geo-report") -> None:
    """Generate report markdown from template."""
    template = ROOT / "reports" / "templates" / "geo_report_template.md"
    output_dir = ROOT / "reports"
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / f"{report_name}.md"
    shutil.copyfile(template, output)
    print(f"[green]Generated report template:[/green] {output}")


if __name__ == "__main__":
    app()
