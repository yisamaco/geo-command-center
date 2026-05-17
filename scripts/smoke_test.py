from __future__ import annotations

import json
import urllib.request

BASE = "http://localhost:8000/api/v1"
PATHS = [
    "/health",
    "/llm-platforms",
    "/knowledge/entities",
    "/geo/runs",
]


def get(path: str):
    with urllib.request.urlopen(f"{BASE}{path}", timeout=10) as r:
        return json.loads(r.read().decode("utf-8"))


def main() -> None:
    print("Running backend smoke test...")
    for path in PATHS:
        payload = get(path)
        size = len(payload) if isinstance(payload, list) else 1
        print(f"OK {path} -> {size} record(s)")
    print("Smoke test passed.")


if __name__ == "__main__":
    main()
