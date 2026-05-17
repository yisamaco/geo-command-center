insert into llm_platforms
  (name, company, ecosystem, country, default_access_method, supports_api, supports_openai_compatible, supports_search, supports_citation, supports_browser_access, status)
values
  ('OpenAI', 'OpenAI', 'global', 'US', 'api', true, false, true, true, true, 'active'),
  ('Claude', 'Anthropic', 'global', 'US', 'api', true, false, true, true, true, 'active'),
  ('Gemini', 'Google', 'global', 'US', 'api', true, false, true, true, true, 'active'),
  ('Perplexity', 'Perplexity AI', 'global', 'US', 'search_api', true, true, true, true, true, 'active'),
  ('Copilot', 'Microsoft', 'global', 'US', 'api', true, false, true, false, true, 'active'),
  ('Grok', 'xAI', 'global', 'US', 'api', true, true, true, false, true, 'active'),
  ('Mistral', 'Mistral AI', 'global', 'FR', 'api', true, true, false, false, true, 'active'),
  ('Cohere', 'Cohere', 'global', 'CA', 'api', true, false, false, false, true, 'active'),
  ('You.com', 'You.com', 'global', 'US', 'search_api', true, false, true, true, true, 'active'),
  ('Qwen', 'Alibaba Cloud', 'china', 'CN', 'api', true, true, true, true, true, 'active'),
  ('DeepSeek', 'DeepSeek', 'china', 'CN', 'api', true, true, true, true, true, 'active'),
  ('Doubao', 'ByteDance', 'china', 'CN', 'browser', false, false, true, true, true, 'active'),
  ('Kimi', 'Moonshot AI', 'china', 'CN', 'browser', true, true, true, true, true, 'active'),
  ('Wenxin', 'Baidu', 'china', 'CN', 'api', true, false, true, true, true, 'active'),
  ('Yuanbao', 'Tencent', 'china', 'CN', 'browser', false, false, true, false, true, 'active'),
  ('Zhipu GLM', 'Zhipu AI', 'china', 'CN', 'api', true, true, true, true, true, 'active'),
  ('讯飞星火', 'iFlytek', 'china', 'CN', 'api', true, false, true, false, true, 'active'),
  ('MiniMax', 'MiniMax', 'china', 'CN', 'api', true, true, true, false, true, 'active'),
  ('秘塔 AI', 'Metaso', 'china', 'CN', 'browser', false, false, true, true, true, 'active'),
  ('夸克 AI', 'Quark', 'china', 'CN', 'browser', false, false, true, true, true, 'active'),
  ('百度 AI 搜索', 'Baidu', 'china', 'CN', 'search_api', true, false, true, true, true, 'active'),
  ('360 智脑', '360', 'china', 'CN', 'browser', false, false, true, false, true, 'active')
on conflict (name) do nothing;
