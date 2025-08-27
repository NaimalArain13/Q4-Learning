import asyncio
from agents import Agent, RunContextWrapper, function_tool,Runner
from connection import config
from rich import print
from pydantic import BaseModel

# class BankAccount(BaseModel):
#     account_number:str
#     customer_name:str
#     account_balance:float
#     account_type:str
# class LibraryBook(BaseModel):
#     book_id:str
#     book_title:str
#     author_name:str
#     is_available:bool
# class CombineData(BankAccount, LibraryBook):
#     pass

# @function_tool
# def get_info(ctx:RunContextWrapper[CombineData]):
#     if isinstance(ctx.context, BankAccount):
#         return f"Account number: {ctx.context.account_number}, Customer name: {ctx.context.customer_name}, Account balance: {ctx.context.account_balance}, Account type: {ctx.context.account_type}"
#     elif isinstance(ctx.context, LibraryBook):
#         return f"Book ID: {ctx.context.book_id}, Book title: {ctx.context.book_title}, Author name: {ctx.context.author_name}, Is available: {ctx.context.is_available}"
#     else:
#         return "Invalid context"
class SmartContext(BaseModel):
    account_number: str
    customer_name: str
    account_balance: float
    account_type: str
    book_id: str
    book_title: str
    author_name: str
    is_available: bool

@function_tool
def smart_extract_info(ctx: RunContextWrapper[SmartContext]):
    """Extract relevant information based on context"""
    print("Smart extraction called...")
    
    # Return all data, let agent decide what to use
    return {
        "bank_info": {
            "account_number": ctx.context.account_number,
            "customer_name": ctx.context.customer_name,
            "account_balance": ctx.context.account_balance,
            "account_type": ctx.context.account_type
        },
        "book_info": {
            "book_id": ctx.context.book_id,
            "book_title": ctx.context.book_title,
            "author_name": ctx.context.author_name,
            "is_available": ctx.context.is_available
        }
    }

smart_agent = Agent(
    name="Smart Agent",
    instructions="""
    You can access both bank and book information using smart_extract_info tool.
    
    When user asks a question:
    1. Call the tool to get all available data
    2. Extract and present ONLY the information relevant to the user's question
    3. Ignore irrelevant data
    
    For example:
    - If asked about a book, only mention book details
    - If asked about account, only mention bank details
    - If asked generally, provide relevant summary
    """,
    tools=[smart_extract_info],
)

async def test_smart_approach():
    print("\n" + "="*60)
    print("TESTING SMART APPROACH")
    print("="*60)
    
    smart_context = SmartContext(
        account_number="ACC-789456",
        customer_name="Fatima Khan",
        account_balance=75500.50,
        account_type="savings",
        book_id="B-123456",
        book_title="The Great Gatsby",
        author_name="F. Scott Fitzgerald",
        is_available=True
    )
    
    result = await Runner.run(
        smart_agent,
        "Give me details of 'The Great Gatsby'",
        run_config=config,
        context=smart_context
    )
    
    print(f"Smart Agent Response: {result.final_output}")
asyncio.run(test_smart_approach())