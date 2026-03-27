# 🤖 Claude AI Agent Examples

A collection of simple AI agents built with Python and the Anthropic SDK.

## Examples

### ☕ Starbucks Finder (`starbucks_agent.py`)
Finds nearby Starbucks locations in any city using web search.

### 🌤️ Weather Agent (`weather_agent.py`)
Gets live weather data for any city using the free Open-Meteo API (no API key needed).

## Installation
```bash
pip3 install anthropic ddgs
```

## Setup

Set your Anthropic API key:
```bash
export ANTHROPIC_API_KEY="your-key-here"
```

## Usage
```bash
python3 starbucks_agent.py
python3 weather_agent.py
```

## How It Works

Each agent follows the same simple loop:
1. You give Claude a question
2. Claude decides which tool to use
3. Your code runs the tool and returns results
4. Claude reads the results and answers
