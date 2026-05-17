import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Route, Routes, Link } from "react-router-dom";
import { Refine } from "@refinedev/core";

import { DashboardPage } from "./pages/dashboard";
import { SimpleListPage } from "./pages/simple-list";
import type { GeoRun, KnowledgeEntity, LLMPlatform } from "./types";

function App() {
  return (
    <BrowserRouter>
      <Refine>
        <div style={{ fontFamily: "sans-serif", padding: 16 }}>
          <h1>GEO Command Center</h1>
          <nav style={{ display: "flex", gap: 12, marginBottom: 16, flexWrap: "wrap" }}>
            <Link to="/">Dashboard</Link>
            <Link to="/prompt-monitor">Prompt Monitor</Link>
            <Link to="/geo-runs">GEO Runs</Link>
            <Link to="/knowledge-entities">Knowledge Entities</Link>
            <Link to="/llm-platforms">LLM Platforms</Link>
          </nav>
          <Routes>
            <Route path="/" element={<DashboardPage />} />
            <Route path="/prompt-monitor" element={<SimpleListPage<GeoRun> title="Prompt Monitor" path="/geo/runs" renderRow={(r) => `${r.run_name ?? "(unnamed)"} | ${r.prompt}`} />} />
            <Route path="/geo-runs" element={<SimpleListPage<GeoRun> title="GEO Runs" path="/geo/runs" renderRow={(r) => `${r.run_mode} / ${r.access_method} | ${r.prompt}`} />} />
            <Route path="/knowledge-entities" element={<SimpleListPage<KnowledgeEntity> title="Knowledge Entities" path="/knowledge/entities" renderRow={(e) => `${e.name} (${e.entity_type}) - ${e.short_definition ?? ""}`} />} />
            <Route path="/llm-platforms" element={<SimpleListPage<LLMPlatform> title="LLM Platforms" path="/llm-platforms" renderRow={(p) => `${p.name} | ${p.ecosystem} | ${p.default_access_method}`} />} />
          </Routes>
        </div>
      </Refine>
    </BrowserRouter>
  );
}

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
