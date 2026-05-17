-- GEO Command Center initial MVP schema
-- Order: Database -> Knowledge Graph -> GEO Core

create extension if not exists pgcrypto;

-- enums
create type access_method as enum ('api', 'search_api', 'manual', 'browser');
create type run_mode as enum ('api_geo', 'search_geo', 'manual_geo', 'browser_geo', 'consumer_geo');
create type viewport_type as enum ('desktop', 'mobile');
create type surface_type as enum ('web', 'app');
create type device_type as enum ('desktop', 'mobile', 'android', 'ios');
create type automation_status as enum ('not_started', 'manual_login_required', 'ready', 'failed');
create type entity_type as enum ('company', 'technology', 'process', 'product', 'equipment', 'problem', 'solution', 'material', 'standard', 'term');
create type snippet_type as enum ('definition', 'faq', 'comparison', 'parameter_table', 'use_case', 'limitation', 'misconception');
create type export_type as enum ('markdown', 'json', 'jsonld', 'faq_schema', 'organization_schema', 'product_schema', 'llms_txt', 'knowledge_index_json');

-- layer: llm platform registry
create table if not exists llm_platforms (
  id uuid primary key default gen_random_uuid(),
  name text not null unique,
  company text not null,
  ecosystem text not null check (ecosystem in ('global', 'china')),
  country text not null,
  default_access_method access_method not null,
  supports_api boolean not null default false,
  supports_openai_compatible boolean not null default false,
  supports_search boolean not null default false,
  supports_citation boolean not null default false,
  supports_browser_access boolean not null default true,
  status text not null default 'active',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- layer: GEO monitoring runs
create table if not exists geo_runs (
  id uuid primary key default gen_random_uuid(),
  run_name text,
  prompt text not null,
  llm_platform_id uuid references llm_platforms(id),
  access_method access_method not null,
  run_mode run_mode not null,
  consumer_surface text,
  viewport_type viewport_type,
  surface_type surface_type,
  device_type device_type,
  response_text text,
  response_raw jsonb,
  desktop_screenshot_url text,
  mobile_screenshot_url text,
  html_snapshot_url text,
  browser_profile text,
  automation_driver text,
  automation_status automation_status not null default 'not_started',
  region text not null default 'global',
  language text not null default 'en',
  created_at timestamptz not null default now()
);

create table if not exists geo_scores (
  id uuid primary key default gen_random_uuid(),
  geo_run_id uuid not null references geo_runs(id) on delete cascade,
  score_scope text not null check (score_scope in ('api_geo', 'search_geo', 'browser_geo', 'desktop', 'mobile')),
  brand_mention_score numeric(5,2) not null,
  position_score numeric(5,2) not null,
  citation_accuracy_score numeric(5,2) not null,
  sentiment_score numeric(5,2) not null,
  competitor_dominance_score numeric(5,2) not null,
  total_score numeric(5,2) generated always as (
    round((brand_mention_score + position_score + citation_accuracy_score + sentiment_score + competitor_dominance_score) / 5.0, 2)
  ) stored,
  created_at timestamptz not null default now()
);

-- layer: knowledge graph
create table if not exists knowledge_entities (
  id uuid primary key default gen_random_uuid(),
  entity_type entity_type not null,
  name text not null,
  aliases text[] not null default '{}',
  slug text not null unique,
  short_definition text,
  long_description text,
  canonical_url text,
  language text not null default 'en',
  region text not null default 'global',
  status text not null default 'active',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists knowledge_relationships (
  id uuid primary key default gen_random_uuid(),
  source_entity_id uuid not null references knowledge_entities(id) on delete cascade,
  target_entity_id uuid not null references knowledge_entities(id) on delete cascade,
  relationship_type text not null,
  weight numeric(4,2) not null default 1.0,
  created_at timestamptz not null default now(),
  unique (source_entity_id, target_entity_id, relationship_type)
);

create table if not exists knowledge_snippets (
  id uuid primary key default gen_random_uuid(),
  entity_id uuid not null references knowledge_entities(id) on delete cascade,
  snippet_type snippet_type not null,
  content text not null,
  language text not null default 'en',
  region text not null default 'global',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists knowledge_sources (
  id uuid primary key default gen_random_uuid(),
  entity_id uuid not null references knowledge_entities(id) on delete cascade,
  source_title text not null,
  source_url text,
  source_type text not null default 'web',
  created_at timestamptz not null default now()
);

create table if not exists knowledge_exports (
  id uuid primary key default gen_random_uuid(),
  entity_id uuid not null references knowledge_entities(id) on delete cascade,
  export_type export_type not null,
  content text not null,
  url text,
  generated_at timestamptz not null default now()
);

create index if not exists idx_geo_runs_platform on geo_runs(llm_platform_id);
create index if not exists idx_geo_scores_run on geo_scores(geo_run_id);
create index if not exists idx_knowledge_entities_slug on knowledge_entities(slug);
create index if not exists idx_knowledge_snippets_entity on knowledge_snippets(entity_id);
