import asyncio
from agents import Agent, Runner, enable_verbose_stdout_logging
from connection import config
from rich import print

enable_verbose_stdout_logging()

urdu_agent = Agent(
    name="Urdu Agent",
    instructions="""
    You are an Urdu Lecturer for Higher Education that response to the students question once you are done with the lecutre.
    Lecutre Topic can be any but you will answer based on the query you will recieve.
    """
)
english_agent = Agent(
    name="English Agent",
    instructions="""
    You are an English Lecturer for Higher Education that response to the students question once you are done with the lecutre.
    Lecutre Topic can be any but you will answer based on the query you will recieve.
    """
)
bio_agent = Agent(
    name="Biology Agent",
    instructions="""
    You are an Biology Lecturer for Higher Education that response to the students question once you are done with the lecutre.
    Lecutre Topic can be any but you will answer based on the query you will recieve.
    """
)
phy_agent = Agent(
    name="Pyhsics Agent",
    instructions="""
    You are an Pyhsics Lecturer for Higher Education that response to the students question once you are done with the lecutre.
    Lecutre Topic can be any but you will answer based on the query you will recieve.
    """
)

science_agent = Agent(
    name="Science Agent",
    instructions="""
    You are an expert Science Agent that will transfer the query to the approriate sub-agent.
    You have 2 sub-agent named 'Biology Agent' and 'Physics Agent'.
    If query related to Biology then transfer to biology agent.
    If query related to Physics then transfer to physics agent.
    Always handoffs the query to the appropriate agent do no answer the user yourself.
    """,
    handoffs=[phy_agent, bio_agent]
)

education_agent = Agent(
    name= "Education Agent",
    instructions="""
            You are an educational agent that transfer the query to the provided sub-agent, 
            You have 3 sub-agents:
            1-English Agent- Transfer the query to English Agent if query is related to english.
            2-Urdu Agent- Transfer the query to Urdu Agent if query is related to urdu.
            3-Science Agent- Tansfer the query to Science Agent if query is related to science.
    """,
    handoffs=[urdu_agent, english_agent, science_agent]
)

async def main():
    result =await Runner.run(education_agent, "Explain how fish breathe.", run_config=config)
    print(result.last_agent.name)
    print(result.final_output)
    
    
asyncio.run(main())