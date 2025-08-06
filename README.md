## Tasks Overview

## Leader Group Assignments
### **Task 01: Research on Generative AI**
An overview of generative AI, including how it works, key concepts (like deep learning, transformers, and diffusion models), and its applications in text, image, and audio generation.

### **Task 02: Learn About FastAPI**
Introduction to FastAPI, a modern Python web framework for building fast and efficient APIs with automatic docs, asynchronous support, and easy integration with modern Python features.

### **Task 03: Pydantic**
Explores how Pydantic is used in FastAPI for data validation and type enforcement using Python type hints, ensuring robust and clean data handling.

### **Task 04: FastAPI Parameters**
Covers how to use query parameters, path parameters, request bodies, and more in FastAPI endpoints to build dynamic and flexible APIs.

### **Task 05: Dependency Injection in FastAPI**
An explanation of FastAPI’s built-in dependency injection system, which allows for clean, modular code and easy sharing of resources like database connections or authentication logic.

###  **Task 06: Task Tracker API**

📝 Project: Task Tracker API
📦 Overview
Implement an API that manages Users and their Tasks, with:

🚀 Requirements
Pydantic Models & Validation

Define UserCreate and UserRead models inheriting BaseModel. 

Use EmailStr for email validation. 

Constrain username to 3–20 characters using constr.

Ensure due_date ≥ today via a @validator. 

FastAPI Endpoints

Users
POST /users/ – create a user (return UserRead).

GET /users/{user_id} – retrieve user.

Tasks
POST /tasks/ – create a task (return full Task model).

GET /tasks/{task_id} – get task.

PUT /tasks/{task_id} – update status only, validating allowed values. 

GET /users/{user_id}/tasks – list all tasks for a user.


💡Hint

Store data in two global dicts:
USERS: dict[int, User] = {}
TASKS: dict[int, Task] = {}


### **Task 07: OpenAI Agent SDK**
An introduction to OpenAI’s Agent SDK, which allows developers to build AI agents that can use tools, call APIs, and carry out tasks in structured, controlled environments.

### **Task 08: What LLM Is?**
A beginner-friendly explanation of Large Language Models (LLMs)—what they are, how they work, their real-world applications, and how they power tools like ChatGPT.

### **Task 09: What is Function/Tool calling?**
A deep research on function/tool calling —what they are, how they work, their real-world applications, and how they power agents.


### **Task 10: Goal: I want to get the current Market Rate of Crypto Currencies.**
Breaking the problem into bullet Points:

1. Install Required Libraries
2. Create an agent named CryptoDataAgent.
3. Binance API/CoinLore: Utilize requests to fetch ticker information (tool calling)
Useful Links:
(CoinLore API)[https://www.coinlore.com/cryptocurrency-data-api?utm_source=chatgpt.com]
(Binance API)[https://api.binance.com/api/v3/ticker/price]
4. Define the Agent’s Workflow (Implement Runner.run)
5. Execute the Agent


### **Task 11: Inner_Working_Function_Tools**
More about Function tooling
Your Task Important for everyone to perform
1. Study the prompts above and extract information from the prompt considering yourself as LLM. Also you guys need to do function implementation and run the code.

2. Explore doc strings.

3. Find the Function_tool response from the result variable after running the code.
Prompt Exercise:
1. What's the weather going to be like in Dubai tomorrow afternoon?

2. Find me some good Chinese restaurants near downtown that are open right now

3. Send an email to Sarah about the project deadline being moved to next Wednesday

4. Schedule a meeting with the marketing team for this Friday at 2 PM about the new campaign

5. I want to buy a wireless Bluetooth headphones under $100 with good reviews

### **Task 12: Hands-on on Hands-off**
Types of Poetry
- Lyric poetry is when poets write about their own feelings and thoughts, like songs or poems about being sad or happy.

- Narrative poetry tells a story with characters and events, just like a regular story but written in poem form with rhymes or special rhythm.

- Dramatic poetry is meant to be performed out loud, where someone acts like a character and speaks their thoughts and feelings to an audience (acting in a theatre).

1. Make a poet agent. Alternatively you could pass a poetry (2 stanza) as an input.
2. Make three analyst agent. 
3. Make a triage/Orchestrator/Parent agent.

Exercise: Make a Triage/Parent agent that gives takes a poetry as an input and Triage/Poetry agent analyze the poetry and handoffs to the appropriate agent. The appropriate analyze agent should give description (tashree) of the poetry.




## Class Assignments:
### **Task 1: Translator Agent.**
Create a simple translator agent. 
 
### **Task 2: Goal: I want to get the current Market Rate of Crypto Currencies.**
Breaking the problem into bullet Points:

1. Install Required Libraries
2. Create an agent named CryptoDataAgent.
3. Binance API/CoinLore: Utilize requests to fetch ticker information (tool calling)
Useful Links:
(CoinLore API)[https://www.coinlore.com/cryptocurrency-data-api?utm_source=chatgpt.com]
(Binance API)[https://api.binance.com/api/v3/ticker/price]
4. Define the Agent’s Workflow (Implement Runner.run)
5. Execute the Agent


### **Task 3: Shopping Agent.**
Use any product data API and fetch the data in function tool then register that tool in your agent and ask relevant question and see how the agent response your query. 


### **Task 4: Hands-on on Hands-off**
Types of Poetry
- Lyric poetry is when poets write about their own feelings and thoughts, like songs or poems about being sad or happy.

- Narrative poetry tells a story with characters and events, just like a regular story but written in poem form with rhymes or special rhythm.

- Dramatic poetry is meant to be performed out loud, where someone acts like a character and speaks their thoughts and feelings to an audience (acting in a theatre).

1. Make a poet agent. Alternatively you could pass a poetry (2 stanza) as an input.
2. Make three analyst agent. 
3. Make a triage/Orchestrator/Parent agent.

Exercise: Make a Triage/Parent agent that gives takes a poetry as an input and Triage/Poetry agent analyze the poetry and handoffs to the appropriate agent. The appropriate analyze agent should give description (tashree) of the poetry.


### **Task 4: Input Guardrails**

Exercise # 1 Objective: Make a agent and make an input guardrail trigger. Prompt: I want to change my class timings 😭😭 Outcome: After running the above prompt an InputGuardRailTripwireTriggered in except should be called. See the outcome in LOGS

Exercise # 2 Objective: Make a father agent and father guardrail. The father stopping his child to run below 26C.

Exercise # 3 Objective: Make a gate keeper agent and gate keeper guardrail. The gate keeper stopping students of other school.

Exercise: Make a Triage/Parent agent that gives takes a poetry as an input and Triage/Poetry agent analyze the poetry and handoffs to the appropriate agent. The appropriate analyze agent should give description (tashree) of the poetry.
