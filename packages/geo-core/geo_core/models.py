from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class AccessMethod(str, Enum):
    api = "api"
    search_api = "search_api"
    manual = "manual"
    browser = "browser"


class ScoreScope(str, Enum):
    api_geo = "api_geo"
    search_geo = "search_geo"
    browser_geo = "browser_geo"
    desktop = "desktop"
    mobile = "mobile"


@dataclass(slots=True)
class GeoScore:
    scope: ScoreScope
    brand_mention: float
    position: float
    citation_accuracy: float
    sentiment: float
    competitor_dominance: float

    @property
    def total(self) -> float:
        return round(
            (self.brand_mention + self.position + self.citation_accuracy + self.sentiment + self.competitor_dominance) / 5.0,
            2,
        )
