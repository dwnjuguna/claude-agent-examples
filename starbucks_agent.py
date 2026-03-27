import anthropic
import json
from ddgs import DDGS

client = anthropic.Anthropic()

# --- Define the tool ---
tools = [
    {
        "name": "find_nearby_starbucks",
        "description": "Search for the nearest Starbucks locations in a given city or area.",
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
    }
]

# --- Tool runner ---
def run_tool(name, inputs):
    if name == "find_nearby_starbucks":
        location = inputs["location"]
        query = f"Starbucks locations near {location} address hours"
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))
            return json.dumps(results)
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
run_agent("Find me the nearest Starbucks in Union Square, San Francisco")
