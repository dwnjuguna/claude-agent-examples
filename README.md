# ☕🌤️ Starbucks Finder + Weather Agent

A combined AI agent built with Python and the Anthropic SDK that finds nearby Starbucks locations **and** fetches live weather data for any city — all in a single run.

---

## What It Does

Ask the agent about a city and it will:
- ☕ Find nearby Starbucks locations with addresses and opening hours
- 🌤️ Fetch the current live weather (temperature, wind speed, conditions)
- 📋 Combine both results into a single, clean response

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

### 2. Set your API key

Replace `your-key-here` with your actual Anthropic API key:

```bash
export ANTHROPIC_API_KEY="your-key-here"
```

---

## Usage

### Run the agent

```bash
python3 starbucks_weather_agent.py
```

### Example Output

```
User: Find me the nearest Starbucks locations with opening hours in San Francisco, California, and also tell me the current weather there.

🔧 Claude is using tool: find_nearby_starbucks with input: {'location': 'San Francisco, California'}
🔧 Claude is using tool: get_weather with input: {'city': 'San Francisco'}

Claude:
## Current Weather in San Francisco
| Condition      | Value         |
|----------------|---------------|
| 🌡️ Temperature | 80.2°F        |
| 💨 Wind Speed  | 2.2 mph       |
| ☁️ Conditions  | Partly cloudy |
| 🌞 Daytime     | Yes           |

## Starbucks Locations in San Francisco
San Francisco has 64 Starbucks locations...
```

### Change the city

To search a different city, update the last line of `starbucks_weather_agent.py`:

```python
run_agent("Find me the nearest Starbucks locations with opening hours in Austin, Texas, and also tell me the current weather there.")
```

---

## How It Works

The agent uses two tools running in a single loop:

| Tool | Description | API Used |
|------|-------------|----------|
| `find_nearby_starbucks` | Searches for Starbucks locations and hours | DuckDuckGo (free) |
| `get_weather` | Fetches live weather data | Open-Meteo (free, no key needed) |

### Agent Loop

1. User sends a message
2. Claude decides which tools to call
3. Your code runs the tools and returns real data
4. Claude reads the results and combines them into one response
5. Loop ends when Claude is done

---

## Project Structure

```
claude-agent-examples/
│
├── starbucks_weather_agent.py   # Combined Starbucks + Weather agent
├── starbucks_agent.py           # Starbucks finder only
├── weather_agent.py             # Weather only
└── README.md                    # This file
```

---

## Troubleshooting

### SSL Certificate Error on Mac
If you see `SSL: CERTIFICATE_VERIFY_FAILED`, run:
```bash
/Applications/Python\ 3.X/Install\ Certificates.command
```
Replace `3.X` with your Python version (e.g. `3.14`).

### `ddgs` package warning
If you see a warning about `duckduckgo_search` being renamed, make sure you have the correct package installed:
```bash
pip3 install ddgs
```

---

## Dependencies

| Package | Purpose | Cost |
|---------|---------|------|
| `anthropic` | Claude AI SDK | Paid (per API call) |
| `ddgs` | DuckDuckGo web search | Free |
| `certifi` | SSL certificates for Mac | Free |
| Open-Meteo | Live weather API (built-in, no install needed) | Free |

---

## Resources

- [Anthropic Documentation](https://docs.anthropic.com)
- [Anthropic API Console](https://console.anthropic.com)
- [Tool Use Guide](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)
- [Open-Meteo Weather API](https://open-meteo.com)
