from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import typer

app = typer.Typer(help="Browser runner placeholder for Consumer GEO")

SESSION_DIR = Path(".browser-session")
SNAPSHOT_DIR = Path("reports/browser-snapshots")


@app.command("init-session")
def init_session(profile: str = "default") -> None:
    """Initialize persistent browser session folder (manual login placeholder)."""
    target = SESSION_DIR / profile
    target.mkdir(parents=True, exist_ok=True)
    (target / "README.txt").write_text(
        "Manual login required. This folder represents a persistent browser profile for MVP.\n",
        encoding="utf-8",
    )
    typer.echo(f"Session initialized: {target}")


@app.command("capture")
def capture(surface: str, viewport: str = "desktop", profile: str = "default") -> None:
    """Create placeholder screenshot/html snapshot metadata for manual testing."""
    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    out = SNAPSHOT_DIR / f"{surface}-{viewport}-{now}.md"
    out.write_text(
        "\n".join(
            [
                f"# Browser Snapshot Placeholder",
                f"- surface: {surface}",
                f"- viewport: {viewport}",
                f"- profile: {profile}",
                f"- captured_at_utc: {now}",
                "- screenshot_url: pending://manual-capture",
                "- html_snapshot_url: pending://manual-snapshot",
                "",
                "This is an MVP placeholder. Real Playwright capture is intentionally deferred.",
            ]
        ),
        encoding="utf-8",
    )
    typer.echo(f"Snapshot placeholder written: {out}")


if __name__ == "__main__":
    app()
