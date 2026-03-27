import anthropic
import json
import urllib.request
import urllib.parse
import ssl
import certifi
from ddgs import DDGS

client = anthropic.Anthropic()

# --- SSL fix for Mac ---
ssl_context = ssl.create_default_context()
ssl_context.load_verify_locations(cafile=certifi.where())

# --- Define the tools ---
tools = [
    {
        "name": "find_nearby_starbucks",
        "description": "Search for the nearest Starbucks locations and their opening hours in a given city or area.",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city or area to search for Starbucks locations"
                }
            },
            "required": ["location"]
        }
    },
    {
        "name": "get_weather",
        "description": "Get the current weather for a given city. Use only the city name, no state or country.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The city name only, no state or country (e.g. 'San Francisco' not 'San Francisco, California')"
                }
            },
            "required": ["city"]
        }
    }
]

# --- Starbucks search using DuckDuckGo ---
def find_starbucks(location):
    query = f"Starbucks locations near {location} address opening hours"
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=5))
        return json.dumps(results)

# --- Weather using Open-Meteo (free, no API key needed) ---
def fetch_url(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, context=ssl_context) as response:
        return json.loads(response.read())

def get_coordinates(city):
    # Strip anything after a comma to get just the city name
    city = city.split(",")[0].strip()
    encoded_city = urllib.parse.quote(city)
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={encoded_city}&count=1"
    data = fetch_url(url)
    if "results" not in data or len(data["results"]) == 0:
        return None, None, None
    result = data["results"][0]
    return result["latitude"], result["longitude"], result["name"]

def get_weather(city):
    lat, lon, resolved_name = get_coordinates(city)
    if lat is None:
        return json.dumps({"error": f"Could not find coordinates for {city}"})
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&current_weather=true"
        f"&temperature_unit=fahrenheit"
        f"&windspeed_unit=mph"
    )
    data = fetch_url(url)
    weather = data.get("current_weather", {})
    return json.dumps({
        "city": resolved_name,
        "temperature_f": weather.get("temperature"),
        "windspeed_mph": weather.get("windspeed"),
        "weather_code": weather.get("weathercode"),
        "is_day": weather.get("is_day")
    })

# --- Tool router ---
def run_tool(name, inputs):
    if name == "find_nearby_starbucks":
        return find_starbucks(inputs["location"])
    elif name == "get_weather":
        return get_weather(inputs["city"])
    return "Tool not found."

# --- The agent loop ---
def run_agent(user_message):
    print(f"\nUser: {user_message}\n")
    messages = [{"role": "user", "content": user_message}]

    while True:
        response = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=2048,
            tools=tools,
            messages=messages
        )

        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    print(f"🔧 Claude is using tool: {block.name} with input: {block.input}")
                    result = run_tool(block.name, block.input)
                    print(f"🔧 Tool result: {result}")
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
                    print(f"Claude: {block.text}")
            break

# --- Run it! ---
run_agent("Find me the nearest Starbucks locations with opening hours in San Francisco, California, and also tell me the current weather there.")
