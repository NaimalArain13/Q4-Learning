import asyncio
from agents import Agent, Runner, RunContextWrapper, trace
from pydantic import BaseModel
from connection import config
from dotenv import load_dotenv

load_dotenv()


## Homework:
## Exercise 2: Airline Seat Preference Agent (Intermediate-Advanced)
# Requirement: Build a dynamic instructions system for an airline booking agent that customizes responses based on seat_preference and travel_experience.

# Window + First-time: Explain window benefits, mention scenic views, reassure about flight experience
# Middle + Frequent: Acknowledge the compromise, suggest strategies, offer alternatives
# Any + Premium: Highlight luxury options, upgrades, priority boarding

# Context Fields: seat_preference (window/aisle/middle/any), travel_experience (first_time/occasional/frequent/premium)

class AirlineSeat(BaseModel):
    seat_preference:str
    travel_experience:str
    user_name:str

# Example Instances
# airline_obj=AirlineSeat(user_name="Naimal",seat_preference="Window", travel_experience="First-time")
# airline_obj=AirlineSeat(user_name="Naimal",seat_preference="Aisle", travel_experience="Ocassional")
# airline_obj=AirlineSeat(user_name="Naimal",seat_preference="Middle", travel_experience="Frequent")
airline_obj=AirlineSeat(user_name="Naimal",seat_preference="Any", travel_experience="Premium")

# Way 01:
# def dynamic_instruction_for_airline_seat(ctx: RunContextWrapper[AirlineSeat], agent: Agent[AirlineSeat]):
#     seat_preference=ctx.context.seat_preference
#     travel_experience=ctx.context.travel_experience
#     return (
#         "Explain window benefits, mention scenic views, reassure about flight experience"
#         if seat_preference == "Window" and travel_experience == "First-time"
#         else "Acknowledge the compromise, suggest strategies, offer alternatives"
#         if seat_preference == "Middle" and travel_experience == "Frequent"
#         else "Highlight luxury options, upgrades, priority boarding"
#         if seat_preference == "Any" and travel_experience == "Premium"
#         else "Answer user according to the user type"
#     )

# Way 02:
def dynamic_instruction_for_airline_seat(ctx: RunContextWrapper[AirlineSeat], agent: Agent[AirlineSeat]):
    seat_preference = ctx.context.seat_preference
    travel_experience = ctx.context.travel_experience
    user_name = ctx.context.user_name
    
    base_instructions = {
        ("Window", "First-time"): "Explain window benefits, mention scenic views, reassure about flight experience.",
        ("Middle", "Frequent"): "Acknowledge the compromise, suggest strategies, offer alternatives.",
        ("Any", "Premium"): "Highlight luxury options, upgrades, priority boarding."
    }
    
    greetings = {
        "First-time": f"Hello {user_name}, welcome aboard! I know this is your first time, so let me guide you step by step.",
        "Occasional": f"Hi {user_name}, great to see you flying again! Let’s make this trip smooth and comfortable.",
        "Frequent": f"Welcome back {user_name}! As a frequent traveler, here are some tips tailored for you.",
        "Premium": f"Greetings {user_name}, thank you for choosing our premium service. Let’s ensure your journey is luxurious and seamless."
    }
    
    instruction = base_instructions.get(
        (seat_preference, travel_experience),
        "Provide general seat guidance and reassure about the journey."
    )
    greeting = greetings.get(travel_experience, f"Hello {user_name}, let’s get started with your booking.")
    
    return f"{greeting} Then, based on your preferences: {instruction}"

airline_agent = Agent(
    name="Airline Seat Agent",
    instructions=dynamic_instruction_for_airline_seat
)


async def main():
    with trace("Airline Seat Preference"):
        result = await Runner.run(
            airline_agent,
            "I need to book a flight",
            run_config=config,
            context=airline_obj
        )
        
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
