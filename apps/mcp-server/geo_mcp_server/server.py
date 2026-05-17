from __future__ import annotations

from fastmcp import FastMCP
from sqlalchemy import text

from .db import make_engine

mcp = FastMCP("geo-command-center")


@mcp.tool
def geo_run_prompt(prompt: str, platform: str = "OpenAI", access_method: str = "api") -> dict:
    engine = make_engine()
    with engine.begin() as conn:
        platform_id = conn.execute(text("select id from llm_platforms where name=:name limit 1"), {"name": platform}).scalar()
        run_id = conn.execute(
            text(
                """
                insert into geo_runs (run_name, prompt, llm_platform_id, access_method, run_mode, language, region)
                values (:run_name, :prompt, :llm_platform_id, :access_method, 'manual_geo', 'en', 'global')
                returning id
                """
            ),
            {
                "run_name": f"MCP run - {platform}",
                "prompt": prompt,
                "llm_platform_id": platform_id,
                "access_method": access_method,
            },
        ).scalar()
    return {"run_id": str(run_id), "status": "created"}


@mcp.tool
def geo_compare_models(prompt: str, platform_a: str, platform_b: str) -> dict:
    return {
        "prompt": prompt,
        "platform_a": platform_a,
        "platform_b": platform_b,
        "note": "MVP placeholder. Use geo_run_prompt twice and compare results in analytics layer.",
    }


@mcp.tool
def geo_check_brand_visibility(brand: str, limit: int = 10) -> dict:
    engine = make_engine()
    with engine.begin() as conn:
        rows = conn.execute(
            text(
                """
                select id, prompt, response_text, created_at
                from geo_runs
                where coalesce(response_text, '') ilike :kw
                order by created_at desc
                limit :limit
                """
            ),
            {"kw": f"%{brand}%", "limit": limit},
        ).mappings().all()
    return {"brand": brand, "matches": [dict(r) for r in rows]}


@mcp.tool
def geo_generate_optimization_tasks(brand: str) -> dict:
    return {
        "brand": brand,
        "tasks": [
            "补充品牌定义与核心差异化描述（knowledge_entities.short_definition）",
            "补充FAQ片段并覆盖竞品对比（knowledge_snippets: faq/comparison）",
            "发布llms.txt与knowledge-index.json并复测API/Browser分数",
        ],
    }


@mcp.tool
def geo_generate_article(topic: str) -> dict:
    return {"topic": topic, "content": f"# {topic}\n\nMVP article placeholder."}


@mcp.tool
def geo_generate_faq(topic: str) -> dict:
    return {"topic": topic, "faq": [{"q": f"What is {topic}?", "a": "MVP FAQ placeholder."}]}


@mcp.tool
def geo_generate_schema(entity_name: str, schema_type: str = "organization") -> dict:
    return {"entity_name": entity_name, "schema_type": schema_type, "jsonld": {"@context": "https://schema.org"}}


@mcp.tool
def geo_generate_llms_txt() -> dict:
    engine = make_engine()
    with engine.begin() as conn:
        rows = conn.execute(text("select name, short_definition from knowledge_entities order by name")).all()
    lines = ["# llms.txt", "", "## Knowledge Entities"] + [f"- {name}: {short_definition or ''}" for name, short_definition in rows]
    return {"llms_txt": "\n".join(lines)}


@mcp.tool
def geo_get_knowledge_entity(slug: str) -> dict:
    engine = make_engine()
    with engine.begin() as conn:
        row = conn.execute(
            text("select id, entity_type, name, slug, short_definition, long_description, canonical_url from knowledge_entities where slug=:slug limit 1"),
            {"slug": slug},
        ).mappings().first()
    return {"entity": dict(row) if row else None}


@mcp.tool
def geo_search_knowledge(query: str, limit: int = 10) -> dict:
    engine = make_engine()
    with engine.begin() as conn:
        rows = conn.execute(
            text(
                """
                select id, name, slug, short_definition
                from knowledge_entities
                where name ilike :kw or coalesce(short_definition, '') ilike :kw
                order by name
                limit :limit
                """
            ),
            {"kw": f"%{query}%", "limit": limit},
        ).mappings().all()
    return {"query": query, "results": [dict(r) for r in rows]}


@mcp.tool
def geo_export_knowledge(slug: str, export_type: str = "markdown") -> dict:
    engine = make_engine()
    with engine.begin() as conn:
        entity = conn.execute(
            text("select id, name, short_definition from knowledge_entities where slug=:slug limit 1"), {"slug": slug}
        ).mappings().first()
        if not entity:
            return {"error": f"entity not found: {slug}"}
        content = f"# {entity['name']}\n\n{entity['short_definition'] or ''}" if export_type == "markdown" else "{}"
        export_id = conn.execute(
            text(
                "insert into knowledge_exports (entity_id, export_type, content) values (:entity_id, :export_type, :content) returning id"
            ),
            {"entity_id": entity["id"], "export_type": export_type, "content": content},
        ).scalar()
    return {"export_id": str(export_id), "slug": slug, "export_type": export_type}


@mcp.tool
def geo_export_report(report_name: str = "geo-mvp-report") -> dict:
    return {
        "report_name": report_name,
        "note": "MVP placeholder. Reporting layer will generate structured report files in /reports.",
    }


def run() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    run()
