from agents import function_tool

# 1. What's the weather going to be like in Dubai tomorrow afternoon?
# What to find === weather
# Where to find === in Dubai
# When to find === tomorrow afternoon
@function_tool(
    name_override="Weather_Tool",
    description_override="A tool that can get the current weather of a city"
)
def get_current_weather(city:str, time:str,)->str:
    return f"The weather in {city} at {time} is sunny"


# 2. Find me some good Chinese restaurants near downtown that are open right now
# What to find === Chinese restaurants
# Where to find === near downtown
# When to find === open right now
@function_tool
def get_good_cuisine(cuisine:str, location:str, time:str)->str:
    return f"The best {cuisine} restaurants in {location} that are open right now are {location}"


# 3. Send an email to Sarah about the project deadline being moved to next Wednesday
# What to send === an email
# Whom to send ===  to Sarah
# Email body === tell Sarah that project deadline being moved to next Wednesday
@function_tool
def send_email(to:str,subject:str,body:str)->str:
    return f"Email sent to {to} with subject {subject} and body {body}"

# 4. Schedule a meeting with the marketing team for this Friday at 2 PM about the new campaign
# What to do === Scheduling a meeting
# With whom ===  with marketing team
# When to schedule (date & time) === this friday at 2 PM
# Meeting Agenda === Discussing new campaign
@function_tool
def schedule_meeting(with_whom:str,date:str,time:str,agenda:str)->str:
    return f"Meeting scheduled with {with_whom} on {date} at {time} about {agenda}"

# 5. I want to buy a wireless Bluetooth headphones under $100 with good reviews
# What to do ===  to buy
# what to buy ===  a wirelese Bluetooth headphones 
# Price range ===  under $100 
# Extra requirements === good reviews
@function_tool
def buy_product(product:str,price:str,reviews:str)->str:
    return f"Product {product} bought with price {price} and reviews {reviews}"