# 📊 MarTech Stack Health Agent

An interactive AI agent built with Python and the Anthropic SDK that analyzes any company's MarTech stack across 5 categories, scores its operational efficiency out of 100, and delivers consultant-quality recommendations.

---

## What It Does

Type any company name and the agent will:

- 🔍 **Detect their full MarTech stack** — CRM, Marketing Automation, Analytics, Data & Integration, Advertising
- 🏥 **Research tool health** — deprecations, migrations, known issues per tool
- 🔗 **Check integrations** — data flow gaps and connector issues between tools
- 📊 **Score each category** out of 20 points (100 total)
- ✅ **Deliver top recommendations** to improve stack efficiency
- 📋 **Produce an executive summary** with overall health rating

---

## Example Output

```
You: Anthropic

🔧 Running: detect martech stack — Anthropic...
🔧 Running: research tool health — Salesforce...
🔧 Running: research tool health — Clay...
🔧 Running: research tool health — HubSpot...
🔧 Running: research industry benchmarks — SaaS...
🔧 Running: check integrations — Anthropic...
🔧 Running: research tool health — Google Analytics...
🔧 Running: research tool health — Segment...
🔧 Running: research tool health — LinkedIn Ads...
🔧 Running: research tool health — Google Ads...

# MarTech Stack Health Report: Anthropic
Assessment Date: March 2026
Industry: AI/SaaS/Enterprise Technology

## 1. Detected MarTech Stack
| Category               | Tools Detected                         |
|------------------------|----------------------------------------|
| CRM                    | Salesforce                             |
| Marketing Automation   | HubSpot                                |
| Data & Integration     | Clay                                   |
| Analytics              | Google Analytics 4                     |
| Advertising            | LinkedIn Ads, Google Ads               |

## 2. Stack Health Score: 78/100 🟡
| Category                    | Score | Assessment                              |
|-----------------------------|-------|-----------------------------------------|
| CRM Health                  | 17/20 | Salesforce current, strategically aligned |
| Marketing Automation Health | 14/20 | HubSpot solid but overlaps with Salesforce |
| Analytics Health            | 14/20 | GA4 standard; no product analytics gap |
| Data & Integration Health   | 18/20 | Clay→Salesforce best-in-class           |
| Advertising Health          | 15/20 | LinkedIn Ads appropriate; attribution gap |

## 3. Key Findings
🟢 Clay→Salesforce integration: 3x enrichment coverage, best practice
⚠️ HubSpot Projects v2025.1 deprecating August 1, 2026
💡 HubSpot + Salesforce overlap creating data conflicts

## 4. Top Recommendations
1. Consolidate CRM: Choose Salesforce OR HubSpot (HIGH priority)
2. Add product analytics: Mixpanel or Amplitude for Claude usage (HIGH)
3. Migrate HubSpot before August 2026 deadline (MEDIUM)
4. Implement multi-touch attribution for ad spend (MEDIUM)
5. Add CDP layer: Segment or RudderStack at scale (LOW-MEDIUM)

## 5. Overall Assessment
🟡 Needs Attention (78/100)
Strong sales ops infrastructure. Consolidate CRM strategy,
add product analytics, and prepare for platform migrations.
```

---

## Prerequisites

- Python 3.10+
- An [Anthropic API key](https://console.anthropic.com)

---

## Installation

### 1. Install dependencies

```bash
pip3 install anthropic ddgs certifi
```

### 2. Fix SSL certificates (Mac only)

```bash
/Applications/Python\ 3.X/Install\ Certificates.command
```

Replace `3.X` with your Python version (e.g. `3.14`).

### 3. Set your Anthropic API key

```bash
export ANTHROPIC_API_KEY="your-anthropic-key-here"
```

---

## Usage

```bash
python3 martech_health_agent.py
```

### Input examples

```
You: Anthropic
You: HubSpot
You: Nike
You: Shopify
```

Type `quit` or `exit` to stop.

---

## How It Works

The agent runs up to four research tools automatically per company:

| Tool | What it finds |
|------|--------------|
| `detect_martech_stack` | All tools used across all 5 MarTech categories |
| `research_tool_health` | Deprecations, migrations, known issues per tool |
| `check_integrations` | Data flow gaps and connector issues between tools |
| `research_industry_benchmarks` | Industry best practices to benchmark against |

### Health Scoring Criteria

| Category | Max Points | What it measures |
|----------|-----------|-----------------|
| CRM Health | 20 | Adoption, data quality, version currency |
| Marketing Automation Health | 20 | Deliverability, automation maturity |
| Analytics Health | 20 | Tracking completeness, data accuracy |
| Data & Integration Health | 20 | Connector reliability, data flow gaps |
| Advertising Health | 20 | Attribution coverage, spend efficiency |

### Overall Health Ratings

| Score | Rating |
|-------|--------|
| 80 - 100 | 🟢 Healthy |
| 60 - 79 | 🟡 Needs Attention |
| Below 60 | 🔴 At Risk |

---

## Project Structure

```
claude-agent-examples/
│
├── martech_health_agent.py      # ⭐ MarTech stack health agent
├── lead_enrichment_agent.py     # Lead enrichment + scoring agent
├── interactive_agent.py         # Starbucks + weather interactive agent
├── starbucks_weather_agent.py   # Combined Starbucks + weather (fixed city)
├── starbucks_agent.py           # Starbucks finder only
├── weather_agent.py             # Weather only
├── agent.py                     # General web search agent
├── SETUP.md                     # Detailed setup guide
├── CHANGELOG.md                 # Version history
├── .gitignore                   # Prevents API keys from being uploaded
└── README.md                    # This file
```

---

## Troubleshooting

| Error | Fix |
|-------|-----|
| `command not found: pip` | Use `pip3` instead |
| `SSL: CERTIFICATE_VERIFY_FAILED` | Run the Install Certificates command above |
| `ModuleNotFoundError: ddgs` | Run `pip3 install ddgs` |
| `AuthenticationError` | Check your `ANTHROPIC_API_KEY` is set correctly |
| Agent asks for company name instead of analyzing | Make sure you have the latest version of the file |

---

## Resources

- [Anthropic Documentation](https://docs.anthropic.com)
- [Anthropic API Console](https://console.anthropic.com)
- [Tool Use Guide](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)
