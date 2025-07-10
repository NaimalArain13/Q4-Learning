import asyncio
from connection import config
from agents import Agent, Runner
from rich import print
from tool import buy_product, get_current_weather, get_good_cuisine, schedule_meeting, send_email

async def main():
    agent  =Agent(
        name="Weather Agent",
        instructions="You are a weather agent that can get the current weather of a city",
        tools=[get_current_weather,get_good_cuisine,send_email,schedule_meeting,buy_product],
        model=config.model,   
    )


    runner = await Runner.run(agent, input="I want to buy an earbuds under $500 rating 4.5 and good reviews.",run_config=config)
    print(runner.final_output)

    # print(print(agent.tools))
    
    # for tool in agent.tools: 
    #     print("-------------------------------- Tool Start --------------------------------")
    #     print(tool.name)
    #     print(tool.description)
    #     print(tool.params_json_schema)
    #     print(tool.is_enabled)
    #     print(tool.on_invoke_tool)
    #     print("-------------------------------- Tool End --------------------------------")
asyncio.run(main())