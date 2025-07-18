import asyncio
from dataclasses import dataclass
from hand_off import lyric_agent, narrative_agent, daramatic_agent
from agents import Agent,Runner, enable_verbose_stdout_logging,set_tracing_disabled
from connection import config
from rich import print
enable_verbose_stdout_logging()
set_tracing_disabled(True)

@dataclass
class OutputFormat:
    userInput: str
    style:str
    agent_name:str
    response:str
    

async def main():
    poetry_agent = Agent(
        name="poetry Agent",
        instructions="""You are an orchestrate agent, you will be given a user input which has some stanzas then you need to find what style of the poem is it like lyric, narrative (Descriptive) or dramatic.
        then you will handoff the task to the respective agent based on the style of the poem.
        then you will return the final output in the format of the OutputFormat class.
        Remember, do not write a poem by yourself, you will handoff the task to the respective agent based on the style of the poem.""",
        handoffs=[lyric_agent, narrative_agent, daramatic_agent],
        output_type=OutputFormat,
    )
    runner = await Runner.run(
        starting_agent=poetry_agent,
        input="""Thunder roars across the blackened sky,
Lightning splits the world in burning white,
The earth trembles beneath the storm's wild cry,
As shadows dance in flickering candlelight.""",
        run_config=config,
    )
      # Get the final output (this returns an OutputFormat instance)
    final_output = runner.final_output
    # print(final_output)
    
    # Print the structured output
    print("=== Final Output✨ ===")
    print(f"👤 User Input: {final_output.userInput}")
    print(f"😎 Style: {final_output.style}")
    print(f"🤖 Agent Name: {final_output.agent_name}")
    print(f"💬 Response: {final_output.response}")

    

asyncio.run(main())
