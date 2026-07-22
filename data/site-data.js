/**
 * Correctover Site Data — 全局数据源
 * 所有页面数字、规则、漏洞记录统一来源
 * 数据来源验证（2026-07-22）
 */
window.CORRECTOVER_DATA = {
  brand: {
    name: "Correctover",
    tagline: "AI Runtime Security",
    description: "Real-time RCE, SSRF & Credential Protection for Production AI Workloads",
    email: "wangguigui@correctover.com",
    github: "https://github.com/correctover/mcp-server",
  },
  stats: {
    interceptLatency: { value: "14.5", unit: "µs", label: "P50 Intercept Latency" },
    ccsRules: { value: 24, label: "CCS Detection Rules" },
    productionTraces: { value: "80K", label: "Production Traces", detail: "20K public + 60K internal" },
    validatedFindings: { value: "1,730+", label: "Validated Findings", detail: "CCS v4.2 across 11 frameworks" },
    providers: { value: 13, label: "AI Providers" },
    models: { value: 33, label: "Models" },
    p50Latency: { value: "22", unit: "µs", label: "P50 Validation" },
    p99Latency: { value: "99", unit: "µs", label: "P99 Latency" },
    falsePositiveRate: { value: "<0.3%", label: "False Positive Rate" },
    bountyDisclosures: { value: 7, label: "Responsible Disclosures" },
  },
  vulnerabilities: [
    { id: "MSRC-2025-001", product: "CrewAI", type: "RCE", cvss: "9.8", date: "2025-12" },
    { id: "ZDI-2025-002", product: "AutoGen", type: "RCE", cvss: "9.8", date: "2025-12" },
    { id: "GHSA-2025-003", product: "LiteLLM", type: "SSRF", cvss: "8.6", date: "2026-01" },
    { id: "GHSA-2025-004", product: "Haystack", type: "RCE", cvss: "9.8", date: "2026-02" },
    { id: "GHSA-2025-005", product: "AG2", type: "RCE", cvss: "9.8", date: "2026-03" },
    { id: "GHSA-2025-006", product: "LlamaIndex", type: "RCE", cvss: "9.8", date: "2026-03" },
    { id: "ZDI-2025-007", product: "Docker MCP", type: "Container Escape", cvss: "8.8", date: "2026-04" },
  ],
  mcp: {
    version: "1.1.0",
    packageName: "correctover-mcp-server",
    registries: {
      npm: "https://www.npmjs.com/package/correctover-mcp-server",
      github: "https://github.com/correctover/mcp-server",
      glama: "https://glama.ai/mcp/servers/w0t3c6v41a",
      smithery: "https://smithery.ai/server/@correctover/mcp-server",
    },
    install: {
      npx: "npx correctover-mcp-server",
      pip: "pip install correctover-mcp-server",
    },
    features: ["6-dimension contract validation","Self-healing failover","BYOK encryption","Zero-dependency binary (5MB)"],
  },
};
