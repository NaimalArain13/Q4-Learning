from agents import Agent, function_tool, Runner
from dotenv import load_dotenv
import os
from rich import print
load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")
agent = Agent(
    name="Gemini Agent",
    
)








