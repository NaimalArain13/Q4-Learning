import asyncio
from typing import Dict
from agents import Agent , Runner, function_tool, RunContextWrapper, enable_verbose_stdout_logging
from connection import config
from pydantic import BaseModel
from rich import print
# enable_verbose_stdout_logging()


class UserInfo(BaseModel):
    name:str
    age:int
    address:Dict[str,str]
class ContextOutput(BaseModel):
    user_info:UserInfo
@function_tool
def context(ctx:RunContextWrapper[UserInfo])->ContextOutput:
    # return f"User info: {ctx.context.name},{ctx.context.age},{ctx.context.address}"
    # return ContextOutput(user_info=ctx.context)
    return f"User info: {ctx.context.name},{ctx.context.age},{ctx.context.address['city']},{ctx.context.address['state']},{ctx.context.address['country']}"

personal_agent = Agent[UserInfo](
    name="Personal Agent",
    instructions="""
    You are a helpful assistant that can help with personal related questions.
    Greet the user first with his name,
    For example: "Hello ALI, how can I help you today?"
    You have all the personal information through the local context and you will be responsible to provide the appropriate information to the end user and those information which you do not have then politely decline to the user.
    """,
    tools=[context]

)
triage_agent = Agent(
    name="Triage Agent",
    instructions="""
    You are a helpful assistant who always transfer teh query to the animal agent.
    """,
    tools=[context],
    handoffs=[personal_agent]
    
)


async def main():
    user_info = UserInfo(
        name="Sarah",
        age=25,
        address={"city":"New York", "state":"NY", "country":"USA"}
    )
    result = await Runner.run(triage_agent, "Whats my address?",run_config=config,context=user_info)
    print(result.final_output)
    print(result.last_agent.name)

if __name__ == "__main__":
    asyncio.run(main())
