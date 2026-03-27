import anthropic
import json
import urllib.request

client = anthropic.Anthropic()

# --- Define the tool ---
tools = [
    {
        "name": "get_weather",
        "description": "Get the current weather for a given city.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The city to get weather for (e.g. 'San Francisco, California')"
                }
            },
            "required": ["city"]
        }
    }
]

# --- Tool runner using Open-Meteo (free, no API key needed) ---
def get_coordinates(city):
    """Look up lat/lon for a city using the Open-Meteo geocoding API."""
    encoded_city = urllib.parse.quote(city)
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={encoded_city}&count=1"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
    if "results" not in data or len(data["results"]) == 0:
        return None, None, None
    result = data["results"][0]
    return result["latitude"], result["longitude"], result["name"]

def run_tool(name, inputs):
    if name == "get_weather":
        import urllib.parse
        city = inputs["city"]
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
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())

        weather = data.get("current_weather", {})
        return json.dumps({
            "city": resolved_name,
            "temperature_f": weather.get("temperature"),
            "windspeed_mph": weather.get("windspeed"),
            "weather_code": weather.get("weathercode"),
            "is_day": weather.get("is_day")
        })
    return "Tool not found."

# --- The agent loop ---
def run_agent(user_message):
    print(f"\nUser: {user_message}\n")
    messages = [{"role": "user", "content": user_message}]

    while True:
        response = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=1024,
            tools=tools,
            messages=messages
        )

        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    print(f"🔧 Claude is using tool: {block.name} with input: {block.input}")
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
                    print(f"Claude: {block.text}")
            break

# --- Run it! ---
run_agent("What is the current weather in San Francisco, California?")
