import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Route, Routes, Link } from "react-router-dom";
import { Refine } from "@refinedev/core";

import { DashboardPage } from "./pages/dashboard";
import { SimpleListPage } from "./pages/simple-list";

function App() {
  return (
    <BrowserRouter>
      <Refine>
        <div style={{ fontFamily: "sans-serif", padding: 16 }}>
          <h1>GEO Command Center</h1>
          <nav style={{ display: "flex", gap: 12, marginBottom: 16 }}>
            <Link to="/">Dashboard</Link>
            <Link to="/prompt-monitor">Prompt Monitor</Link>
            <Link to="/geo-runs">GEO Runs</Link>
            <Link to="/knowledge-entities">Knowledge Entities</Link>
            <Link to="/llm-platforms">LLM Platforms</Link>
          </nav>
          <Routes>
            <Route path="/" element={<DashboardPage />} />
            <Route path="/prompt-monitor" element={<SimpleListPage title="Prompt Monitor" />} />
            <Route path="/geo-runs" element={<SimpleListPage title="GEO Runs" />} />
            <Route path="/knowledge-entities" element={<SimpleListPage title="Knowledge Entities" />} />
            <Route path="/llm-platforms" element={<SimpleListPage title="LLM Platforms" />} />
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
