# 🎯 Lead Enrichment + Scoring Agent

An interactive AI agent built with Python and the Anthropic SDK that researches any company and contact, then produces a structured lead enrichment report with a score out of 100 and recommended next actions.

---

## What It Does

Type any company name (and optionally a contact name and role) and the agent will:

- 🏢 Research the company — industry, size, HQ, products and services
- 📰 Find recent buying signals — funding rounds, product launches, expansions, hiring shifts
- 👤 Research the contact — role, seniority, responsibilities (if provided)
- 🎯 Score the lead out of 100 with clear reasoning per category
- ✅ Recommend a next action — reach out now, monitor, or low priority

---

## Example Output

```
You: Salesforce

🔍 Researching: research company — Salesforce...
🔍 Researching: search news — Salesforce...

# Lead Enrichment Report: Salesforce

## Company Overview
| Attribute       | Details                                      |
|-----------------|----------------------------------------------|
| Company Name    | Salesforce, Inc.                             |
| Industry        | Cloud-based CRM / Software Development       |
| Headquarters    | San Francisco, California, USA               |
| Company Size    | 10,001+ employees (Enterprise)               |
| Stock           | NYSE: CRM                                    |

## Recent News & Buying Signals
| Signal Type        | Details                                      | Date     |
|--------------------|----------------------------------------------|----------|
| 🔥 Major Investment | Announced $15 billion investment in SF       | Oct 2025 |
| 🚀 Product Launch   | Launched Agentforce 360 AI platform          | Oct 2025 |
| 🤖 AI Focus         | Heavy investment in agentic AI capabilities  | 2025     |

## Lead Score: 75/100
| Criteria              | Score | Reasoning                                      |
|-----------------------|-------|------------------------------------------------|
| Company Size & Growth | 25/30 | Fortune 500 enterprise, mature market leader   |
| Buying Signals        | 22/30 | Major investment signals growth; build vs. buy |
| Contact Relevance     |  0/20 | No contact provided                            |
| Market Timing         | 28/20 | Actively investing in AI transformation        |

## Recommended Next Action
⚠️ MONITOR / IDENTIFY KEY CONTACTS
Salesforce is aggressively investing in AI — consider targeting their
partner ecosystem or identifying a specific decision-maker to enrich further.
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
python3 lead_enrichment_agent.py
```

### Input formats

```
# Company only
You: Salesforce

# Company + contact
You: HubSpot, Jane Doe, VP of Marketing

# Company + contact + role
You: Stripe, John Smith, Head of Partnerships
```

Type `quit` or `exit` to stop.

---

## How It Works

The agent runs up to three research tools automatically:

| Tool | What it does |
|------|-------------|
| `research_company` | Searches for company overview, industry, size, location |
| `search_news` | Finds recent buying signals — funding, launches, hiring, expansions |
| `research_person` | Researches the contact's role and responsibilities (if provided) |

### Lead Scoring Criteria

| Category | Max Points | What it measures |
|----------|-----------|-----------------|
| Company Size & Growth | 30 | Employee count, revenue signals, market position |
| Buying Signals | 30 | Recent funding, product launches, expansions |
| Contact Relevance | 20 | Seniority and decision-making authority |
| Market Timing | 20 | Industry trends and timing fit |

---

## Project Structure

```
claude-agent-examples/
│
├── lead_enrichment_agent.py     # ⭐ Lead enrichment + scoring agent
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

---

## Resources

- [Anthropic Documentation](https://docs.anthropic.com)
- [Anthropic API Console](https://console.anthropic.com)
- [Tool Use Guide](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)
