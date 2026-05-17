from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class EntityType(str, Enum):
    company = "company"
    technology = "technology"
    process = "process"
    product = "product"
    equipment = "equipment"
    problem = "problem"
    solution = "solution"
    material = "material"
    standard = "standard"
    term = "term"


class SnippetType(str, Enum):
    definition = "definition"
    faq = "faq"
    comparison = "comparison"
    parameter_table = "parameter_table"
    use_case = "use_case"
    limitation = "limitation"
    misconception = "misconception"


@dataclass(slots=True)
class KnowledgeEntity:
    entity_type: EntityType
    name: str
    slug: str
    aliases: list[str] = field(default_factory=list)
    short_definition: str = ""
    long_description: str = ""
    canonical_url: str = ""
    language: str = "en"
    region: str = "global"
    status: str = "active"


@dataclass(slots=True)
class KnowledgeSnippet:
    entity_slug: str
    snippet_type: SnippetType
    content: str
    language: str = "en"
    region: str = "global"


@dataclass(slots=True)
class KnowledgeExport:
    entity_slug: str
    export_type: str
    content: str
    url: str = ""
    generated_at: datetime = field(default_factory=datetime.utcnow)
