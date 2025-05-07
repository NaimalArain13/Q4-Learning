# 🚀 FastAPI Login and Item Management API

This project is a basic FastAPI application that includes:
- A hardcoded login system
- Item management APIs (`GET`, `POST`, `PUT`) with query and path parameters
- Fully interactive auto-generated API documentation via Swagger and ReDoc

---

## 📦 Features

- ✅ FastAPI-powered backend
- ✅ Pydantic model for data validation
- ✅ Clear error handling with `HTTPException`
- ✅ Auto-generated Swagger and ReDoc API documentation
- ✅ Easy testing via browser or API clients like Postman/Thunder Client

---

## 🛠️ Setup Instructions

### 1. 🔁 Fork & Clone the Repository

Fork the project and clone it to your local system:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
````

---

### 2. 🌐 (Optional) Install `uv` Globally

`uv` is a faster Python package manager (alternative to `pip`). You can install it for better performance:

#### On macOS/Linux:

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

#### On Windows (CMD/PowerShell):

```powershell
powershell -ExecutionPolicy Bypass -Command "irm https://astral.sh/uv/install.ps1 | iex"
```

---

### 3. 🐍 Create and Activate a Virtual Environment

Create a virtual environment to isolate project dependencies:

```bash
python -m venv venv
```

Activate it:

* macOS/Linux:

  ```bash
  source venv/bin/activate
  ```
* Windows:

  ```bash
  venv\Scripts\activate
  ```

---

### 4. 📦 Install Required Dependencies

Using `uv` (recommended):

```bash
uv pip install fastapi uvicorn
```

Or using traditional `pip`:

```bash
pip install fastapi uvicorn
```

---

### 5. ▶️ Run the FastAPI Server

```bash
uvicorn main:app --reload
```

You can now open your browser and go to:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📂 Project Structure

```
your-repo-name/
│
├── main.py               # All FastAPI routes
├── README.md             # Project documentation (this file)
└── requirements.txt      # (Optional) List of dependencies
```

---

## 🧪 API Testing Guide

### 1. `GET /`

* **Description:** Basic greeting endpoint.
* **URL:** `/`
* **Method:** GET
* **Response:**

```json
{
  "greeting": "hello from naimal"
}
```

---

### 2. `POST /login`

* **Description:** Hardcoded login API
* **Method:** POST
* **Query Parameters:**

  * `email` (string): must be `naimalarain@gmail.com`
  * `password` (string): must be `admin123`

#### ✅ Success Response:

```json
{
  "message": "login Successful"
}
```

#### ❌ Failure Response:

```json
{
  "detail": "Please enter the correct password, Here are the hard-coded crendentials email:naimalarain@gmail.com, password:admin123"
}
```

---

### 3. `GET /items/{item_id}`

* **Description:** Fetch item with optional query
* **Method:** GET
* **Path Parameter:**

  * `item_id` (integer)
* **Query Parameter (optional):**

  * `q` (string)

#### Example:

Request: `/items/2?q=books`

#### Response:

```json
{
  "item_id": 2,
  "q": "books"
}
```

---

### 4. `PUT /items/{item_id}`

* **Description:** Update item details
* **Method:** PUT
* **Path Parameter:**

  * `item_id` (integer)
* **Request Body:** JSON based on `ItemType` model:

```json
{
  "name": "Banana",
  "price": 5.99,
  "is_offer": true
}
```

#### Response:

```json
{
  "item_name": "Banana",
  "item_id": 1,
  "item_price": 5.99,
  "is_offer": true
}
```

---

## 📄 Optional: `requirements.txt`

you can install the required dependencies with the command below:

```bash
pip install -r requirements.txt
```

---

## 🔐 Security Note

> This project uses **hardcoded credentials** for educational purposes only.
> Never use this method in production environments.

---

## 🧠 Useful Tips

* All APIs can be tested from [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* You can also use tools like **Postman**, **Thunder Client (VS Code)**, or **cURL**

