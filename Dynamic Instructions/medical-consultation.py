import asyncio
from agents import Agent, Runner, RunContextWrapper, trace
from pydantic import BaseModel
from connection import config
from dotenv import load_dotenv

load_dotenv()


## Homework:
## Exercise 1: Medical Consultation Assistant (Intermediate)
# Requirement: Create a dynamic instructions system for a medical consultation agent that adapts based on user_type.

# Patient: Use simple, non-technical language. Explain medical terms in everyday words. Be empathetic and reassuring.
# Medical Student: Use moderate medical terminology with explanations. Include learning opportunities.
# Doctor: Use full medical terminology, abbreviations, and clinical language. Be concise and professional.
class MedicalConsultation(BaseModel):
    user_name:str
    user_type:str

# Example Instances
# medical_obj=MedicalConsultation(user_name="Naimal", user_type="Patient")
# medical_obj=MedicalConsultation(user_name="Naimal", user_type="Medical Student")
medical_obj=MedicalConsultation(user_name="Naimal", user_type="Doctor")

# Way 01:
# def dynamic_instruction_for_medical_consultation(ctx: RunContextWrapper[MedicalConsultation], agent: Agent[MedicalConsultation]):
#     return (
#         "Use simple, non-technical language. Explain medical terms in everyday words. Be empathetic and reassuring."
#         if ctx.context.user_type == "Patient"
#         else "Use moderate medical terminology with explanations. Include learning opportunities."
#         if ctx.context.user_type == "Medical Student"
#         else "Use full medical terminology, abbreviations, and clinical language. Be concise and professional."
#         if ctx.context.user_type == "Doctor"
#         else "Answer user according to the user type"
#     )

# Way 02:
def dynamic_instruction_for_medical_consultation(ctx: RunContextWrapper[MedicalConsultation], agent: Agent[MedicalConsultation]):
    user_name = ctx.context.user_name
    user_type = ctx.context.user_type
    
    base_instructions = {
        "Patient": "Use simple, non-technical language. Explain medical terms in everyday words. Be empathetic and reassuring.",
        "Medical Student": "Use moderate medical terminology with explanations. Include learning opportunities.",
        "Doctor": "Use full medical terminology, abbreviations, and clinical language. Be concise and professional."
    }
    
    return f"Start by greeting the user by name: '{user_name}'. Then follow these instructions: {base_instructions.get(user_type, 'Answer user according to the user type')}."

medical_agent = Agent(
    name="Medical Agent",
    instructions=dynamic_instruction_for_medical_consultation
)


async def main():
    with trace("Medical Consultation"):
        result = await Runner.run(
            medical_agent,
            "What is Obesity",
            run_config=config,
            context=medical_obj
        )
        
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
