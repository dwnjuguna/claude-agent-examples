# Changelog

All notable changes to this project are documented here.

---

## v3.0 — Interactive Agent

### Added
- `interactive_agent.py` — fully interactive agent that accepts any city typed directly in the Terminal
- Google Places API integration for real Starbucks locations with addresses, phone numbers, ratings, and live open/closed status
- Google Geocoding API integration for accurate city-to-coordinates lookup
- System prompt to ensure Claude always calls both tools immediately without asking clarifying questions
- Permanent SSL fix using `certifi` for Mac compatibility

### Fixed
- Removed secondary `get_place_details` API call that was causing silent failures
- Starbucks results now use data returned directly from the initial Places API call

---

## v2.0 — Combined Starbucks + Weather Agent

### Added
- `starbucks_weather_agent.py` — single agent that runs both Starbucks and weather tools together
- DuckDuckGo web search for Starbucks locations (`ddgs` package)
- Open-Meteo weather API integration (free, no API key required)
- SSL certificate fix for Mac using `certifi`

---

## v1.0 — Individual Agents

### Added
- `agent.py` — general web search agent using DuckDuckGo
- `starbucks_agent.py` — Starbucks finder using DuckDuckGo web search
- `weather_agent.py` — live weather using Open-Meteo API
- Basic Anthropic SDK tool use implementation
