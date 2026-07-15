import os
import re
import urllib.request
import json

def get_stars(repo):
    try:
        url = f"https://api.github.com/repos/{repo}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data.get('stargazers_count', 0)
    except:
        return 0

# Create assets folder and SVG banner
os.makedirs('assets', exist_ok=True)
svg_banner = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#4facfe;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#00f2fe;stop-opacity:1" />
    </linearGradient>
    <style>
      .title { font-size: 40px; font-weight: bold; fill: #ffffff; font-family: sans-serif; }
      .subtitle { font-size: 20px; fill: #e0e0e0; font-family: sans-serif; }
      .circle { animation: pulse 3s infinite; }
      @keyframes pulse { 0% { r: 5; opacity: 0.5; } 50% { r: 15; opacity: 1; } 100% { r: 5; opacity: 0.5; } }
    </style>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad)" rx="15" ry="15" />
  <circle cx="700" cy="100" r="10" fill="#ffffff" class="circle" />
  <circle cx="650" cy="50" r="7" fill="#ffffff" class="circle" style="animation-delay: 1s;" />
  <circle cx="750" cy="150" r="12" fill="#ffffff" class="circle" style="animation-delay: 2s;" />
  <text x="50" y="90" class="title">Awesome AI-Powered Data Analyst 🚀</text>
  <text x="50" y="130" class="subtitle">A curated list of AI-Powered Data Analysis Tools &amp; Frameworks</text>
</svg>"""

with open('assets/banner.svg', 'w', encoding='utf-8') as f:
    f.write(svg_banner)

# We will just rewrite the README completely to accommodate all changes
new_readme = """# Awesome AI-Powered Data Analyst 🤖📊

<div align="center">
  <img src="assets/banner.svg" alt="Awesome AI-Powered Data Analyst Banner" />
</div>

<p align="center">
  <a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a>
  <a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>
  <a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>
</p>

## 🌟 Top AI-Powered Data Analyst Tools & Open-Source Alternatives

A comprehensive, SEO-optimized curated guide to leading **SaaS/cloud-hosted AI-Powered Data Analyst tools** and their **open-source/self-hosted equivalents**. 

**Open-source solutions are emphasized** for customization, data privacy, cost control, and building AI-driven analytics on your infrastructure. 🏢

---

## ☁️ SaaS / Cloud-Hosted AI Data Analyst Tools

Popular platforms using LLMs and AI for natural language querying, automated insights, semantic search, and conversational BI. 📈

### 🏆 Leading Options (Sorted by Valuation/Revenue)

| Product | Description | Pricing | Free Tier Limit | Valuation / Size |
|---------|-------------|---------|-----------------|------------------|
| **[Microsoft Power BI Copilot](https://powerbi.microsoft.com)** | AI-assisted report generation and insights in Power BI. | Requires Premium/Fabric capacity | No Free Tier | ~$3 Trillion |
| **[Tableau Pulse](https://tableau.com)** | AI-driven insights and explanations. | Included in Tableau Cloud licenses | No Free Tier | ~$260 Billion (Salesforce) |
| **[Snowflake Cortex Analyst](https://snowflake.com)** | Natural language to SQL with semantic modeling. | Pay-as-you-go (Compute/AI Credits) | No Free Tier | ~$45 Billion |
| **[Databricks AI/BI Genie](https://databricks.com)** | Conversational analytics and agentic insights on lakehouse data. | Pay-as-you-go (Compute) | No Free Tier | ~$43 Billion |
| **[ThoughtSpot](https://thoughtspot.com)** | Search-driven analytics with SpotIQ AI. | Custom / Consumption-based | No Free Tier (Trial only) | ~$4.2 Billion |
| **[Hex](https://hex.tech)** | AI data assistant for notebooks and reporting. | ~$36/user/month | 5 projects, limited compute | ~$300 Million |
| **Tellius** | Search-driven analytics platform. | Custom Enterprise Pricing | No Free Tier | ~$100 Million |
| **[camelAI](https://camelai.com)** | AI data assistant for analysis and coding. | Starting at ~$30/month | 10 messages/week | < $50 Million |
| **[Julius AI](https://julius.ai)** | AI data assistant for analysis and visualization. | Paid plans available | 15 messages/month | < $50 Million |
| **Datost** | AI-powered data analytics. | Custom Pricing | No Free Tier | Early Stage Startup |
| **Skopx** | Generative AI BI tool. | Custom Pricing | No Free Tier | Early Stage Startup |

These tools lower the barrier for non-technical users to explore data via chat interfaces and generate actionable insights. 💡

---

## 🛠️ Open-Source / Self-Hosted Alternatives

These leverage open LLMs, vector search, and semantic layers to create custom AI data analysts with full control. 🔐

### 🌟 Featured Projects (Sorted by GitHub Stars)

- **[LangChain](https://github.com/langchain-ai/langchain)** [![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langchain?style=social&color=white)](https://github.com/langchain-ai/langchain/stargazers) — Frameworks for building natural language to SQL and data agents using open models.
- **[Apache Superset](https://github.com/apache/superset)** [![GitHub stars](https://img.shields.io/github/stars/apache/superset?style=social&color=white)](https://github.com/apache/superset/stargazers) — BI tool with AI extensions or custom LLM plugins for natural language BI.
- **[LlamaIndex](https://github.com/run-llama/llama_index)** [![GitHub stars](https://img.shields.io/github/stars/run-llama/llama_index?style=social&color=white)](https://github.com/run-llama/llama_index/stargazers) — Data framework for your LLM applications.
- **[AutoGen](https://github.com/microsoft/autogen)** [![GitHub stars](https://img.shields.io/github/stars/microsoft/autogen?style=social&color=white)](https://github.com/microsoft/autogen/stargazers) — Custom agents for multi-step data analysis.
- **[Chroma](https://github.com/chroma-core/chroma)** [![GitHub stars](https://img.shields.io/github/stars/chroma-core/chroma?style=social&color=white)](https://github.com/chroma-core/chroma/stargazers) — Vector database for semantic search over data catalogs.
- **[Weaviate](https://github.com/weaviate/weaviate)** [![GitHub stars](https://img.shields.io/github/stars/weaviate/weaviate?style=social&color=white)](https://github.com/weaviate/weaviate/stargazers) — Vector database for semantic search.
- **[Cube.js](https://github.com/cube-js/cube.js)** [![GitHub stars](https://img.shields.io/github/stars/cube-js/cube.js?style=social&color=white)](https://github.com/cube-js/cube.js/stargazers) — Semantic layer combined with open RAG tools.
- **[dbt](https://github.com/dbt-labs/dbt-core)** [![GitHub stars](https://img.shields.io/github/stars/dbt-labs/dbt-core?style=social&color=white)](https://github.com/dbt-labs/dbt-core/stargazers) — dbt Semantic Layer for governed metrics and AI querying.
- **[Trino](https://github.com/trinodb/trino)** [![GitHub stars](https://img.shields.io/github/stars/trinodb/trino?style=social&color=white)](https://github.com/trinodb/trino/stargazers) — Distributed SQL query engine.
- **[LangGraph](https://github.com/langchain-ai/langgraph)** [![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langgraph?style=social&color=white)](https://github.com/langchain-ai/langgraph/stargazers) — Stateful, multi-actor applications with LLMs.
- **[Evidence](https://github.com/evidence-dev/evidence)** [![GitHub stars](https://img.shields.io/github/stars/evidence-dev/evidence?style=social&color=white)](https://github.com/evidence-dev/evidence/stargazers) — AI-augmented notebooks and reports.
- **[Meltano](https://github.com/meltano/meltano)** [![GitHub stars](https://img.shields.io/github/stars/meltano/meltano?style=social&color=white)](https://github.com/meltano/meltano/stargazers) — Data pipelines feeding AI analysts.

**Tip**: Combine **LangChain** agents with your warehouse (Snowflake/Databricks/BigQuery) and open LLMs for a powerful self-hosted AI data analyst. ⚡

---

## ⚖️ Comparison

| Aspect              | SaaS Platforms                        | Open-Source / Self-Hosted                  |
|---------------------|---------------------------------------|--------------------------------------------|
| **Cost** 💸         | Subscription + usage                  | Free (LLM/infra costs)                     |
| **Customization** 🛠️| Limited to vendor models              | Full agent logic, models, and prompts      |
| **Data Privacy** 🛡️ | Cloud-processed data                  | On-prem or VPC deployment                  |
| **Setup Effort** ⏱️ | Quick setup                           | Requires integration & tuning              |
| **Use Case** 🎯     | Teams wanting managed AI BI           | Data teams, privacy-sensitive organizations|

---

## 🚀 Getting Started

1. Choose your data sources and semantic layer (dbt recommended). 🗄️
2. Build a basic agent with **LangChain** or **LlamaIndex**. 🧠
3. Integrate open LLMs and test natural language queries. 💬
4. Add UI (Streamlit/Gradio) for chat interface. 🖥️
5. Deploy securely and iterate on prompts/evaluations. 🔒

## 🤝 Contributing

Feel free to submit PRs to expand this list with more projects, tools, or comparisons! 🎉

**Last updated**: July 2026  
*AI data tools evolve rapidly — always check the latest on GitHub and verify security/compliance.* 🛡️

##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007/Awesome-AI-Powered-Data-Analyst&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-AI-Powered-Data-Analyst&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-AI-Powered-Data-Analyst&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-AI-Powered-Data-Analyst&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_readme)
