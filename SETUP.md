# 🛠️ Setup Guide

Step-by-step instructions to get the Starbucks + Weather agent running on your Mac.

---

## Step 1: Install Python

Download Python 3.10+ from [python.org](https://python.org) and install it.

Verify it installed correctly:
```bash
python3 --version
```

---

## Step 2: Install Dependencies

```bash
pip3 install anthropic ddgs certifi
```

---

## Step 3: Fix SSL Certificates (Mac only)

This is required on Mac to allow Python to make secure web requests:

```bash
/Applications/Python\ 3.X/Install\ Certificates.command
```

Replace `3.X` with your Python version (e.g. `3.14`).

---

## Step 4: Get Your Anthropic API Key

1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up or log in
3. Navigate to **API Keys** and create a new key
4. Copy the key — you'll need it in the next step

---

## Step 5: Set Your API Key

Paste this into your Terminal, replacing `your-key-here` with your actual key:

```bash
export ANTHROPIC_API_KEY="your-key-here"
```

> ⚠️ **Important:** Never commit your API key to GitHub. The `.gitignore` file in this repo is set up to prevent accidentally uploading `.env` files.

---

## Step 6: Run the Agent

```bash
python3 starbucks_weather_agent.py
```

---

## Changing the City

Open `starbucks_weather_agent.py` and update the last line:

```python
run_agent("Find me the nearest Starbucks locations with opening hours in Austin, Texas, and also tell me the current weather there.")
```

---

## Common Issues

| Error | Fix |
|-------|-----|
| `command not found: pip` | Use `pip3` instead of `pip` |
| `SSL: CERTIFICATE_VERIFY_FAILED` | Run the Install Certificates command in Step 3 |
| `ModuleNotFoundError: No module named 'ddgs'` | Run `pip3 install ddgs` |
| `AuthenticationError` | Check your API key is set correctly in Step 5 |
