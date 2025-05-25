import os  
import chainlit as cl 
import google.generativeai as genai  
from dotenv import load_dotenv  
from typing import Optional, Dict

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

@cl.oauth_callback
def oauth_callback(
    provider_id: str,  
    token: str,  
    raw_user_data: Dict[str, str], 
    default_user: cl.User, 
) -> Optional[cl.User]:  
    """
    Handle the OAuth callback from GitHub
    Return the user object if authentication is successful, None otherwise
    """

    print(f"Provider: {provider_id}")  
    print(f"User data: {raw_user_data}")  

    return default_user


@cl.on_chat_start
async def handle_chat_start():
    await cl.Message(content="Hello! how can I help you today?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    prompt = message.content
    response = model.generate_content(prompt)
    response_text = response.text if hasattr(response, "text") else ""
    await cl.Message(content=response_text).send()