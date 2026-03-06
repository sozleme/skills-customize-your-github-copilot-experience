# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build RESTful APIs using the FastAPI framework, practicing API design, routing, request/response handling, and data validation.

## 📝 Tasks

### 🛠️ Set Up FastAPI Application

#### Description
Initialize a FastAPI application and create a basic root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance
- Define a GET endpoint at "/" that returns a JSON response with a welcome message
- Run the server and verify the endpoint works

### 🛠️ Create CRUD Endpoints

#### Description
Implement Create, Read, Update, Delete (CRUD) operations for a simple resource like "items" or "tasks".

#### Requirements
Completed program should:

- Define a data model for the resource using Pydantic
- Create endpoints for:
  - GET /items - retrieve all items
  - POST /items - create a new item
  - GET /items/{id} - retrieve a specific item
  - PUT /items/{id} - update an item
  - DELETE /items/{id} - delete an item
- Use appropriate HTTP status codes
- Handle cases where items don't exist

### 🛠️ Add Request Validation and Error Handling

#### Description
Enhance the API with input validation and proper error responses.

#### Requirements
Completed program should:

- Use Pydantic models for request bodies
- Validate input data (e.g., required fields, data types)
- Return appropriate error responses for invalid requests
- Add custom exception handlers if needed