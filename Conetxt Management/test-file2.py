import asyncio
from agents import Agent, RunContextWrapper, function_tool, Runner
from connection import config
from rich import print
from pydantic import BaseModel

class BankAccount(BaseModel):
    account_number: str
    customer_name: str
    account_balance: float
    account_type: str

class LibraryBook(BaseModel):
    book_id: str
    book_title: str
    author_name: str
    is_available: bool

class CombinedContext(BaseModel):
    bank_data: BankAccount
    book_data: LibraryBook

@function_tool
def get_bank_details(ctx: RunContextWrapper[CombinedContext]):
    """Get bank account information"""
    print("Getting bank account details...")
    bank = ctx.context.bank_data
    return f"Bank Details - Account: {bank.account_number}, Customer: {bank.customer_name}, Balance: ${bank.account_balance}, Type: {bank.account_type}"

@function_tool
def get_book_details(ctx: RunContextWrapper[CombinedContext]):
    """Get library book information"""
    print("Getting book details...")
    book = ctx.context.book_data
    availability = "Available" if book.is_available else "Not Available"
    return f"Book Details - ID: {book.book_id}, Title: {book.book_title}, Author: {book.author_name}, Status: {availability}"

@function_tool
def get_all_details(ctx: RunContextWrapper[CombinedContext]):
    """Get all available information"""
    print("Getting all details...")
    bank = ctx.context.bank_data
    book = ctx.context.book_data
    
    bank_info = f"Bank Account - {bank.account_number}, Customer: {bank.customer_name}, Balance: ${bank.account_balance}"
    book_info = f"Library Book - '{book.book_title}' by {book.author_name}, Available: {book.is_available}"
    
    return f"{bank_info}\n{book_info}"

general_agent = Agent(
    name="General Agent",
    instructions="""
    You are a helpful agent that can access both bank account and library book information.
    
    Use these tools based on user queries:
    - get_bank_details: When user asks about bank account, balance, customer info, or financial details
    - get_book_details: When user asks about books, library, author, or book availability
    - get_all_details: When user asks for complete information or general queries
    
    Analyze the user's question carefully and choose the most appropriate tool.
    Provide clear, relevant answers based on what the user is asking.
    """,
    tools=[get_bank_details, get_book_details, get_all_details],
)

async def main():
    context = CombinedContext(
        bank_data=BankAccount(
            account_number="ACC-789456",
            customer_name="Fatima Khan",
            account_balance=75500.50,
            account_type="savings"
        ),
        book_data=LibraryBook(
            book_id="B-123456",
            book_title="The Great Gatsby",
            author_name="F. Scott Fitzgerald",
            is_available=True
        )
    )
    
    # Different queries
    test_queries = [
        "Give me details of 'The Great Gatsby'",  
        "What is my account balance?",             
        "Tell me about Fatima Khan",               
        "Is the book available?",                  
        "Give me all information",                 
    ]
    
    for query in test_queries:
        print(f"\n" + "="*60)
        print(f"User Query: {query}")
        print("="*60)
        
        result = await Runner.run(
            general_agent, 
            query, 
            run_config=config, 
            context=context
        )
        
        print(f"Agent Response: {result.final_output}")
asyncio.run(main())