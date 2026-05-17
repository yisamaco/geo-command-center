export type LLMPlatform = {
  id: string;
  name: string;
  company: string;
  ecosystem: string;
  country: string;
  default_access_method: string;
  supports_api: boolean;
  supports_openai_compatible: boolean;
  supports_search: boolean;
  supports_citation: boolean;
  supports_browser_access: boolean;
  status: string;
};

export type KnowledgeEntity = {
  id: string;
  entity_type: string;
  name: string;
  slug: string;
  short_definition?: string;
  language: string;
  region: string;
  status: string;
};

export type GeoRun = {
  id: string;
  run_name?: string;
  prompt: string;
  access_method: string;
  run_mode: string;
  consumer_surface?: string;
  viewport_type?: string;
};
