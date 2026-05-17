from __future__ import annotations

import json
from typing import Iterable

from .models import KnowledgeEntity, KnowledgeSnippet


def build_markdown(entity: KnowledgeEntity, snippets: Iterable[KnowledgeSnippet]) -> str:
    sections = [
        f"# {entity.name}",
        "",
        f"**Type:** {entity.entity_type.value}",
        f"**Definition:** {entity.short_definition}",
        "",
    ]
    for snippet in snippets:
        sections.append(f"## {snippet.snippet_type.value}")
        sections.append(snippet.content)
        sections.append("")
    return "\n".join(sections).strip()


def build_json(entity: KnowledgeEntity, snippets: Iterable[KnowledgeSnippet]) -> str:
    payload = {
        "entity": entity.__dict__,
        "snippets": [s.__dict__ for s in snippets],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def build_llms_txt(entities: Iterable[KnowledgeEntity]) -> str:
    lines = ["# llms.txt", "", "## Knowledge Entities"]
    for entity in entities:
        lines.append(f"- {entity.name}: {entity.short_definition}")
    return "\n".join(lines)
