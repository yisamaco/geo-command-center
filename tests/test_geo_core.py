from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def _load_geo_models_module():
    module_path = Path(__file__).resolve().parents[1] / "packages" / "geo-core" / "geo_core" / "models.py"
    spec = importlib.util.spec_from_file_location("geo_core_models", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_geo_score_total_rounding() -> None:
    module = _load_geo_models_module()
    GeoScore = module.GeoScore
    ScoreScope = module.ScoreScope

    score = GeoScore(
        scope=ScoreScope.api_geo,
        brand_mention=70,
        position=72,
        citation_accuracy=68,
        sentiment=75,
        competitor_dominance=60,
    )
    assert score.total == 69.0
