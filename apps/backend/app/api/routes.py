from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.domain import GeoRun, KnowledgeEntity, LLMPlatform
from app.schemas.common import HealthResponse
from app.schemas.geo import GeoRunOut
from app.schemas.knowledge import KnowledgeEntityOut
from app.schemas.platforms import LLMPlatformOut

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse()


@router.get("/llm-platforms", response_model=list[LLMPlatformOut])
def list_llm_platforms(db: Session = Depends(get_db)) -> list[LLMPlatform]:
    return list(db.scalars(select(LLMPlatform).order_by(LLMPlatform.ecosystem, LLMPlatform.name)).all())


@router.get("/knowledge/entities", response_model=list[KnowledgeEntityOut])
def list_knowledge_entities(db: Session = Depends(get_db)) -> list[KnowledgeEntity]:
    return list(db.scalars(select(KnowledgeEntity).order_by(KnowledgeEntity.name)).all())


@router.get("/geo/runs", response_model=list[GeoRunOut])
def list_geo_runs(db: Session = Depends(get_db)) -> list[GeoRun]:
    return list(db.scalars(select(GeoRun).order_by(GeoRun.created_at.desc())).all())
