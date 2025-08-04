import asyncio
from agents import Agent, Runner, function_tool, trace
from dotenv import load_dotenv
from rich import print
from connection import config, gemini_api_key

load_dotenv()
print(gemini_api_key)

english_agent = Agent(
    name="English Agent", 
    instructions="You are a helpful agent. Your task is to answer the user query in English."
)
urdu_agent = Agent(
    name="Urdu Agent", 
    instructions="You are a helpful agent. Your task is to answer the user query in Urdu."
)
Chinese_agent = Agent(
    name="Chinese Agent", 
    instructions="You are a helpful agent. Your task is to answer the user query in Chinese."
)

triage_agent = Agent(
    name="Triage Agent", 
    instructions="You are a helpful agent. Your task is to analyze the user query and delegate it to the appropriate agent.",
    handoffs=[ Chinese_agent,english_agent, urdu_agent]
)



async def main():
   with trace("More on Handoff"):
        runner = await Runner.run(
        triage_agent,
        """I want to learn urdu and also want to learn english.""",
        run_config=config
        )
        print(runner.final_output)
    
    


if __name__ == "__main__":
    asyncio.run(main())
