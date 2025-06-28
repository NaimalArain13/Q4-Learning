## Tasks Overview

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


### **Task 09: Goal: I want to get the current Market Rate of Crypto Currencies.**
Breaking the problem into bullet Points:

1. Install Required Libraries
2. Create an agent named CryptoDataAgent.
3. Binance API: Utilize requests to fetch ticker information (tool calling)
4. Define the Agent’s Workflow (Implement Runner.run)
5. Execute the Agent
