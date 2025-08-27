import asyncio
from agents import Agent, Runner, RunContextWrapper, trace
from pydantic import BaseModel
from connection import config
from dotenv import load_dotenv

load_dotenv()


## Homework:
## Exercise 3: Travel Planning Assistant (Intermediate-Advanced)
# Requirement: Build a dynamic instructions system for a travel planning agent that customizes recommendations based on trip_type and traveler_profile.

# Adventure + Solo: Suggest exciting activities, focus on safety tips, recommend social hostels and group tours for meeting people.
# Cultural + Family: Focus on educational attractions, kid-friendly museums, interactive experiences, family accommodations.
# Business + Executive: Emphasize efficiency, airport proximity, business centers, reliable wifi, Executive lounges.
# medical_student/doctor

class TravelPlanning(BaseModel):
    trip_type:str
    traveler_profile:str
    user_name:str

# Example Instances
airline_obj=TravelPlanning(user_name="Naimal",trip_type="Adventure", traveler_profile="Solo")
# airline_obj=TravelPlanning(user_name="Naimal",trip_type="Cultural", traveler_profile="Family")
# airline_obj=TravelPlanning(user_name="Naimal",trip_type="Business", traveler_profile="Executive")

# Way 01:
# def dynamic_instruction_for_travel_planning(ctx: RunContextWrapper[TravelPlanning], agent: Agent[TravelPlanning]):
#     trip_type=ctx.context.trip_type
#     traveler_profile=ctx.context.traveler_profile
#     return (
#         "Suggest exciting activities, focus on safety tips, recommend social hostels and group tours for meeting people."
#         if trip_type == "Adventure" and traveler_profile == "Solo"
#         else "Focus on educational attractions, kid-friendly museums, interactive experiences, family accommodations."
#         if trip_type == "Cultural" and traveler_profile == "Family"
#         else "Emphasize efficiency, airport proximity, business centers, reliable wifi, Executive lounges."
#         if trip_type == "Business" and traveler_profile == "Executive"
#         else "Answer user according to the user travel profile"
#     )

# Way 02:
def dynamic_instruction_for_travel_planning(ctx: RunContextWrapper[TravelPlanning], agent: Agent[TravelPlanning]):
    trip_type = ctx.context.trip_type
    traveler_profile = ctx.context.traveler_profile
    user_name = ctx.context.user_name
    
    base_instructions = {
        ("Adventure", "Solo"): "Suggest exciting activities, focus on safety tips, recommend social hostels and group tours for meeting people..",
        ("Cultural", "Family"): "Focus on educational attractions, kid-friendly museums, interactive experiences, family accommodations..",
        ("Business", "Executive"): "Emphasize efficiency, airport proximity, business centers, reliable wifi, Executive lounges.."
    }
    
    # greetings customized per traveler_profile
    greetings = {
        "Solo": f"Hey {user_name}, ready for an adventure? Since you’re traveling solo, I’ll help you plan thrilling yet safe experiences.",
        "Family": f"Hi {user_name}, planning a family trip is exciting! Let’s make sure everyone has fun, especially the kids.",
        "Executive": f"Greetings {user_name}, let’s make your business trip smooth and productive with efficient planning.",
        "Occasional": f"Hello {user_name}, great to see you exploring again! Let’s make this trip enjoyable and stress-free."
    }
    
    instruction = base_instructions.get(
        (trip_type, traveler_profile),
        "Provide general travel recommendations and reassure about the journey."
    )
    greeting = greetings.get(traveler_profile, f"Hello {user_name}, let’s get started with your travel planning.")
    
    return f"{greeting} Then, based on your preferences: {instruction}"

travel_agent = Agent(
    name="Travel Planning Agent",
    instructions=dynamic_instruction_for_travel_planning
)


async def main():
    with trace("Travel Planning Preference"):
        result = await Runner.run(
            travel_agent,
            "Give advice for my next trip",
            run_config=config,
            context=airline_obj
        )
        
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
