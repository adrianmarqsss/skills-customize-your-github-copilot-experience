# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to create, read, update, and delete resources. By the end of this assignment, students will understand how to define routes, validate request data, return JSON responses, and document API behavior with FastAPI tools.

## 📝 Tasks

### 🛠️ Set up the FastAPI application

#### Descrição
Create a new FastAPI project with a basic app structure and a health endpoint. Then make sure the app runs locally and returns a JSON response.

#### Requisitos
O programa concluído deve:

- Create a FastAPI application instance.
- Define a root endpoint that returns a welcome message.
- Run the app locally using `uvicorn` or an equivalent development server.
- Verify that the endpoint responds successfully with a JSON payload.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI API"}
```

### 🛠️ Build a CRUD API for items

#### Descrição
Implement a simple item manager with endpoints for listing, creating, retrieving, updating, and deleting records. Use Pydantic models to validate input and ensure predictable API responses.

#### Requisitos
O programa concluído deve:

- Define an `Item` model with fields such as `id`, `name`, and `description`.
- Store items in memory using a list or dictionary.
- Add endpoints to list all items and create a new item.
- Add endpoints to get one item by ID, update it, and delete it.
- Return clear JSON responses for successful and failed requests.

```json
{
  "id": 1,
  "name": "Laptop",
  "description": "A portable computer for coding and study"
}
```

### 🛠️ Improve validation and API documentation

#### Descrição
Refine the API by adding validation rules, error handling, and route-level documentation. This task focuses on making the API more robust and easier for other developers to use.

#### Requisitos
O programa concluído deve:

- Validate required fields and acceptable value constraints using Pydantic.
- Return a helpful 404 response when an item is not found.
- Add endpoint summaries or descriptions to make the API self-explanatory.
- Ensure the app exposes interactive docs at `/docs` and `/redoc`.
- Provide a short explanation of how the API can be tested with `curl` or the Swagger UI.

```bash
curl http://localhost:8000/items
```

---

This assignment introduces the basics of REST API design with FastAPI while keeping the scope realistic for a beginner or intermediate student. Focus on clear route design, input validation, and practical API workflows.
