from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Numeric, String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class LLMPlatform(Base):
    __tablename__ = "llm_platforms"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str] = mapped_column(String)
    company: Mapped[str] = mapped_column(String)
    ecosystem: Mapped[str] = mapped_column(String)
    country: Mapped[str] = mapped_column(String)
    default_access_method: Mapped[str] = mapped_column(String)
    supports_api: Mapped[bool] = mapped_column(Boolean)
    supports_openai_compatible: Mapped[bool] = mapped_column(Boolean)
    supports_search: Mapped[bool] = mapped_column(Boolean)
    supports_citation: Mapped[bool] = mapped_column(Boolean)
    supports_browser_access: Mapped[bool] = mapped_column(Boolean)
    status: Mapped[str] = mapped_column(String)


class KnowledgeEntity(Base):
    __tablename__ = "knowledge_entities"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    entity_type: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    slug: Mapped[str] = mapped_column(String)
    short_definition: Mapped[str | None] = mapped_column(Text)
    long_description: Mapped[str | None] = mapped_column(Text)
    canonical_url: Mapped[str | None] = mapped_column(Text)
    language: Mapped[str] = mapped_column(String)
    region: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)


class GeoRun(Base):
    __tablename__ = "geo_runs"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    run_name: Mapped[str | None] = mapped_column(String)
    prompt: Mapped[str] = mapped_column(Text)
    llm_platform_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("llm_platforms.id"))
    access_method: Mapped[str] = mapped_column(String)
    run_mode: Mapped[str] = mapped_column(String)
    consumer_surface: Mapped[str | None] = mapped_column(String)
    viewport_type: Mapped[str | None] = mapped_column(String)
    response_text: Mapped[str | None] = mapped_column(Text)
    response_raw: Mapped[dict | None] = mapped_column(JSONB)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


class GeoScore(Base):
    __tablename__ = "geo_scores"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    geo_run_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("geo_runs.id"))
    score_scope: Mapped[str] = mapped_column(String)
    brand_mention_score: Mapped[float] = mapped_column(Numeric(5, 2))
    position_score: Mapped[float] = mapped_column(Numeric(5, 2))
    citation_accuracy_score: Mapped[float] = mapped_column(Numeric(5, 2))
    sentiment_score: Mapped[float] = mapped_column(Numeric(5, 2))
    competitor_dominance_score: Mapped[float] = mapped_column(Numeric(5, 2))
