from agent import CryptoDataAgent
from connection import config
from agents import Runner

import asyncio

async def main(input_text):
    runner=await Runner.run(CryptoDataAgent,input=input_text,run_config=config)
    return runner.final_output

