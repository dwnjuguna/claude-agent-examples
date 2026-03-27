# 🛠️ Setup Guide

Complete step-by-step instructions to get all agents running on your Mac.

---

## Step 1: Install Python

Download Python 3.10+ from [python.org](https://python.org) and install it.

Verify it installed correctly:
```bash
python3 --version
```

---

## Step 2: Install Python Dependencies

```bash
pip3 install anthropic ddgs certifi
```

---

## Step 3: Fix SSL Certificates (Mac only)

Required on Mac to allow Python to make secure web requests:

```bash
/Applications/Python\ 3.X/Install\ Certificates.command
```

Replace `3.X` with your Python version (e.g. `3.14`).

Verify it works:
```bash
python3 -c 'import certifi; print("SSL OK:", certifi.where())'
```

---

## Step 4: Get Your Anthropic API Key

1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up or log in
3. Navigate to **API Keys** → **Create New Key**
4. Copy the key

Set it in your Terminal:
```bash
export ANTHROPIC_API_KEY="your-anthropic-key-here"
```

---

## Step 5: Get Your Google Cloud API Key

The interactive agent uses Google Places and Geocoding APIs to find real Starbucks locations.

### 5a. Create a Google Cloud project
1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Click the project dropdown at the top → **New Project**
3. Name it `starbucks-agent` and click **Create**

### 5b. Enable the required APIs
1. Go to **APIs & Services** → **Enable APIs & Services**
2. Search for and enable **Places API**
3. Search for and enable **Geocoding API**

### 5c. Create an API key
1. Go to **APIs & Services** → **Credentials**
2. Click **Create Credentials** → **API Key**
3. Copy the key

Set it in your Terminal:
```bash
export GOOGLE_PLACES_API_KEY="your-google-key-here"
```

> ⚠️ **Important:** Never commit your API keys to GitHub. The `.gitignore` in this repo prevents `.env` files from being uploaded, but always double-check before committing.

---

## Step 6: Verify Everything Works

Test your Google API setup:
```bash
python3 -c "
import urllib.request, urllib.parse, json, ssl, certifi, os
key = os.environ.get('GOOGLE_PLACES_API_KEY')
ctx = ssl.create_default_context()
ctx.load_verify_locations(cafile=certifi.where())
url = f'https://maps.googleapis.com/maps/api/geocode/json?address=Palo+Alto&key={key}'
with urllib.request.urlopen(urllib.request.Request(url), context=ctx) as r:
    print('Google API status:', json.loads(r.read()).get('status'))
"
```

You should see `Google API status: OK`.

---

## Step 7: Run the Interactive Agent

```bash
python3 interactive_agent.py
```

Type any city name and the agent will instantly return nearby Starbucks locations and live weather. Type `quit` to exit.

---

## Common Issues

| Error | Fix |
|-------|-----|
| `command not found: pip` | Use `pip3` instead of `pip` |
| `SSL: CERTIFICATE_VERIFY_FAILED` | Run the Install Certificates command in Step 3 |
| `REQUEST_DENIED` from Google | Make sure both Places API and Geocoding API are enabled in Step 5b |
| `ModuleNotFoundError: No module named 'ddgs'` | Run `pip3 install ddgs` |
| `AuthenticationError` | Check your Anthropic API key is exported correctly in Step 4 |
| `GOOGLE_PLACES_API_KEY not set` | Re-run the export command in Step 5c — keys reset when you open a new Terminal window |

> 💡 **Tip:** API keys set with `export` only last for the current Terminal session. To make them permanent, add the export lines to your `~/.zshrc` file.

---

## Making API Keys Permanent (Optional)

To avoid re-entering your keys every time you open a new Terminal:

```bash
echo 'export ANTHROPIC_API_KEY="your-anthropic-key-here"' >> ~/.zshrc
echo 'export GOOGLE_PLACES_API_KEY="your-google-key-here"' >> ~/.zshrc
source ~/.zshrc
```
