# ☕🌤️ Claude AI Agent Examples

A collection of AI agents built with Python and the Anthropic SDK. Each agent uses real tools to fetch live data — no fake results.

---

## Examples

| File | Description |
|------|-------------|
| `agent.py` | General web search agent using DuckDuckGo |
| `starbucks_agent.py` | Finds nearby Starbucks locations for a fixed city |
| `weather_agent.py` | Fetches live weather for a fixed city |
| `starbucks_weather_agent.py` | Combined Starbucks + weather agent for a fixed city |
| `interactive_agent.py` | ⭐ Full interactive agent — type any city and get real Starbucks locations and live weather instantly |

---

## ⭐ Featured: Interactive Agent

The interactive agent is the most complete example. It lets you type any city directly in the Terminal and instantly returns:

- ☕ Up to 5 nearby Starbucks locations with real addresses, phone numbers, ratings, and live open/closed status
- 🌤️ Current weather including temperature, wind speed, and conditions

### Example Output

```
You: Palo Alto, California

🔧 Looking up find nearby starbucks...
🔧 Looking up get weather...

## ☕ Nearby Starbucks Locations

| # | Name                     | Address                        | Rating         | Phone          | Open Now |
|---|--------------------------|--------------------------------|----------------|----------------|----------|
| 1 | Starbucks Coffee Company | 151 University Ave, Palo Alto  | ⭐ 4.1 (702)   | +1 650-322-6684 | ✅ Yes  |
| 2 | Starbucks Coffee Company | 2190 W Bayshore Rd, Palo Alto  | ⭐ 4.1 (393)   | +1 650-739-0373 | ✅ Yes  |
| 3 | Starbucks Coffee Company | 2000 El Camino Real, Palo Alto | ⭐ 3.7 (570)   | +1 650-320-8125 | ✅ Yes  |

## 🌤️ Current Weather in Palo Alto

| Condition      | Value            |
|----------------|------------------|
| Temperature    | 81°F             |
| Wind Speed     | 5.1 mph          |
| Conditions     | Overcast / Cloudy |
| Time of Day    | Daytime ☀️       |
```

---

## Prerequisites

- Python 3.10+
- [Anthropic API key](https://console.anthropic.com)
- [Google Cloud API key](https://console.cloud.google.com) with these APIs enabled:
  - Places API
  - Geocoding API

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

### 3. Set your API keys

```bash
export ANTHROPIC_API_KEY="your-anthropic-key-here"
export GOOGLE_PLACES_API_KEY="your-google-key-here"
```

---

## Running the Agents

### Interactive agent (recommended)
```bash
python3 interactive_agent.py
```

### Combined Starbucks + weather (fixed city)
```bash
python3 starbucks_weather_agent.py
```

### Starbucks only
```bash
python3 starbucks_agent.py
```

### Weather only
```bash
python3 weather_agent.py
```

### General web search
```bash
python3 agent.py
```

---

## How It Works

Every agent follows the same simple loop:

```
User sends a message
       ↓
Claude decides which tools to call
       ↓
Your code runs the tools and returns real data
       ↓
Claude reads the results and formats a response
       ↓
Loop ends when Claude is done
```

### Tools Used

| Tool | API | Cost |
|------|-----|------|
| Web search | DuckDuckGo (`ddgs`) | Free |
| Starbucks finder | Google Places API | Free tier ($200/month credit) |
| Weather | Open-Meteo | Free, no key needed |

---

## Project Structure

```
claude-agent-examples/
│
├── interactive_agent.py         # ⭐ Interactive Starbucks + weather agent
├── starbucks_weather_agent.py   # Combined agent (fixed city)
├── starbucks_agent.py           # Starbucks finder only
├── weather_agent.py             # Weather only
├── agent.py                     # General web search agent
├── SETUP.md                     # Detailed setup guide
├── .gitignore                   # Prevents API keys from being uploaded
└── README.md                    # This file
```

---

## Troubleshooting

| Error | Fix |
|-------|-----|
| `command not found: pip` | Use `pip3` instead |
| `SSL: CERTIFICATE_VERIFY_FAILED` | Run the Install Certificates command above |
| `REQUEST_DENIED` from Google | Enable the Geocoding API and Places API in Google Cloud Console |
| `ModuleNotFoundError: ddgs` | Run `pip3 install ddgs` |
| `AuthenticationError` | Check your `ANTHROPIC_API_KEY` is set correctly |
| Agent asks questions instead of searching | Make sure you are running the latest `interactive_agent.py` |

---

## Resources

- [Anthropic Documentation](https://docs.anthropic.com)
- [Anthropic API Console](https://console.anthropic.com)
- [Tool Use Guide](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)
- [Google Cloud Console](https://console.cloud.google.com)
- [Open-Meteo Weather API](https://open-meteo.com)
