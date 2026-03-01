from dotenv import load_dotenv
load_dotenv()

from pydantic_ai import Agent, Tool
from .tools import get_weather

weather_tool = Tool(
    name="get_weather",
    description="Fetch weather for a given location.",
    function=get_weather
)

agent = Agent(
    model="gemini-2.5-flash",
    tools=[weather_tool],
    system_prompt=(
        "You are a clothing recommendation assistant. " 
        "Use the weather tool when needed. " 
        "Respond in plain text with friendly, helpful advice."
    ),
)
