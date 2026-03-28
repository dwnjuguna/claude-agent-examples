import anthropic
import json
import os
from ddgs import DDGS

client = anthropic.Anthropic()

# --- System prompt ---
SYSTEM_PROMPT = """You are an expert MarTech stack analyst specializing in operational efficiency and health assessments.

CRITICAL RULES:
- The user will always provide a company name. NEVER ask for one — always start researching immediately.
- Even if the input is just a company name like "Nike" or "Shopify", treat it as a full analysis request.
- Always call detect_martech_stack FIRST, then proceed with the other tools.
- Never ask clarifying questions — just run the analysis.

When given a company name, you will:
1. Use detect_martech_stack to identify the tools the company uses across all MarTech categories
2. Use research_tool_health for each major tool found to check for known issues, deprecations or migrations
3. Use check_integrations to assess how well the tools connect and share data
4. Produce a comprehensive MarTech Stack Health Report

Your final report must always include:

## 1. Detected MarTech Stack
List all tools found organized by category:
- CRM (e.g. Salesforce, HubSpot, Pipedrive)
- Marketing Automation (e.g. Marketo, Pardot, Eloqua, HubSpot)
- Analytics (e.g. GA4, Mixpanel, Amplitude, Adobe Analytics)
- Data & Integration (e.g. Segment, Zapier, MuleSoft, Fivetran)
- Advertising (e.g. Google Ads, Meta Ads, LinkedIn Ads, The Trade Desk)

## 2. Stack Health Score (out of 100)
Score each category out of 20 points:
- CRM Health (20pts): adoption, data quality signals, version currency
- Marketing Automation Health (20pts): deliverability, automation maturity
- Analytics Health (20pts): tracking completeness, data accuracy signals
- Data & Integration Health (20pts): connector reliability, data flow gaps
- Advertising Health (20pts): attribution coverage, spend efficiency signals

## 3. Key Findings
Flag any of these issues if detected:
- ⚠️ Legacy or deprecated tools still in use
- 🔴 Known platform migrations underway
- 🟡 Integration gaps between tools
- 🟢 Best-in-class tools well configured
- 💡 Redundant tools doing the same job

## 4. Efficiency Recommendations
Top 3-5 specific, actionable recommendations to improve stack efficiency.

## 5. Overall Assessment
One paragraph summary with the overall health rating:
- 🟢 Healthy (80-100)
- 🟡 Needs Attention (60-79)
- 🔴 At Risk (below 60)

Always be specific, factual and cite the tools you found. Never invent tools the company does not use.
"""

# --- Define the tools ---
tools = [
    {
        "name": "detect_martech_stack",
        "description": "Research and detect the MarTech tools a company uses across CRM, marketing automation, analytics, data integration and advertising.",
        "input_schema": {
            "type": "object",
            "properties": {
                "company_name": {
                    "type": "string",
                    "description": "The name of the company to research"
                }
            },
            "required": ["company_name"]
        }
    },
    {
        "name": "research_tool_health",
        "description": "Research the current health, known issues, recent updates or deprecation warnings for a specific MarTech tool at a company.",
        "input_schema": {
            "type": "object",
            "properties": {
                "tool_name": {
                    "type": "string",
                    "description": "The name of the MarTech tool (e.g. 'Marketo', 'Salesforce')"
                },
                "company_name": {
                    "type": "string",
                    "description": "The company using the tool"
                }
            },
            "required": ["tool_name", "company_name"]
        }
    },
    {
        "name": "check_integrations",
        "description": "Research how well a company's MarTech tools are integrated and whether there are known data flow gaps or connector issues.",
        "input_schema": {
            "type": "object",
            "properties": {
                "company_name": {
                    "type": "string",
                    "description": "The company to check integrations for"
                },
                "tools": {
                    "type": "string",
                    "description": "Comma separated list of tools to check integrations between"
                }
            },
            "required": ["company_name", "tools"]
        }
    },
    {
        "name": "research_industry_benchmarks",
        "description": "Research MarTech stack benchmarks and best practices for a specific industry to compare against.",
        "input_schema": {
            "type": "object",
            "properties": {
                "industry": {
                    "type": "string",
                    "description": "The industry to research benchmarks for (e.g. 'SaaS', 'ecommerce', 'financial services')"
                }
            },
            "required": ["industry"]
        }
    }
]

# --- Tool implementations ---
def detect_martech_stack(company_name):
    query = f"{company_name} uses CRM marketing automation analytics tools technology stack MarTech"
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=6))
    return json.dumps(results)

def research_tool_health(tool_name, company_name):
    query = f"{company_name} {tool_name} issues migration deprecation update 2024 2025"
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=4))
    return json.dumps(results)

def check_integrations(company_name, tools):
    query = f"{company_name} {tools} integration data pipeline connector issues gaps"
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=4))
    return json.dumps(results)

def research_industry_benchmarks(industry):
    query = f"{industry} MarTech stack best practices benchmarks 2024 2025 tools CRM analytics"
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=4))
    return json.dumps(results)

# --- Tool router ---
def run_tool(name, inputs):
    if name == "detect_martech_stack":
        return detect_martech_stack(inputs["company_name"])
    elif name == "research_tool_health":
        return research_tool_health(inputs["tool_name"], inputs["company_name"])
    elif name == "check_integrations":
        return check_integrations(inputs["company_name"], inputs["tools"])
    elif name == "research_industry_benchmarks":
        return research_industry_benchmarks(inputs["industry"])
    return "Tool not found."

# --- The agent loop ---
def run_agent(user_message):
    messages = [{"role": "user", "content": user_message}]

    while True:
        response = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            tools=tools,
            messages=messages
        )

        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    first_input = list(block.input.values())[0]
                    print(f"🔧 Running: {block.name.replace('_', ' ')} — {first_input}...")
                    result = run_tool(block.name, block.input)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })
            messages.append({"role": "assistant", "content": response.content})
            messages.append({"role": "user", "content": tool_results})

        elif response.stop_reason == "end_turn":
            for block in response.content:
                if hasattr(block, "text"):
                    print(f"\n{block.text}\n")
            break

# --- Interactive loop ---
def main():
    print("\n" + "="*55)
    print("  📊  MarTech Stack Health Agent")
    print("="*55)
    print("Type any company name and I'll analyze their")
    print("MarTech stack across all 5 categories and")
    print("produce a full health and efficiency report.")
    print("Type 'quit' or 'exit' to stop.\n")
    print("Examples:")
    print("  > HubSpot")
    print("  > Shopify")
    print("  > Nike\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["quit", "exit", "q"]:
                print("\nGoodbye! Happy stacking! 📊\n")
                break

            print()
            run_agent(f"Run a full MarTech stack health assessment for: {user_input}")

        except KeyboardInterrupt:
            print("\n\nGoodbye! Happy stacking! 📊\n")
            break

if __name__ == "__main__":
    main()
