# FastAPI Blog Backend

A small backend server built with **FastAPI**, **SQLAlchemy**, and **JWT**.  
It exposes routes for **users**, **blogs**, and **authentication**. Most routes are **protected** and require a Bearer token.

---

## What this project does

- Starts a FastAPI app (`uvicorn blog.main:app`) with interactive docs at:
  - Swagger UI → `http://127.0.0.1:8000/docs`
  - ReDoc → `http://127.0.0.1:8000/redoc`
- Uses **SQLite** for persistence (a `blog.db` file in the `blog/` folder).
- Defines **SQLAlchemy models** for `User` and `Blog`.
- Uses **Pydantic schemas** for request/response validation.
- Hashes passwords with **passlib[bcrypt]**.
- Issues and verifies **JWT access tokens** with **python-jose**.
- Splits logic into **routers**:
  - `authentication` → login + token creation
  - `user` → create/fetch/delete users
  - `blog` → create/fetch/update/delete blogs

---

## Project structure (as in this repo)

blog/ # Python package
├─ init.py
├─ main.py # FastAPI app + router includes
├─ database.py # SQLAlchemy engine, SessionLocal, Base
├─ models.py # ORM models (User, Blog)
├─ schemas.py # Pydantic models (User, Blog, ShowUser, ShowBlog, Token, etc.)
├─ hashing.py # Password hashing/verification helpers
├─ oaut2.py # Dependency: reads/validates JWT and returns current user
├─ token.py # Token creation (JWT encode/expire)
├─ blog.db # SQLite database file (created at runtime)
└─ routers/
├─ authentication.py # POST /login
├─ user.py # user-related routes (create/get/delete)
├─ blog.py # blog-related routes (CRUD)
└─ repository/
├─ authentication.py
├─ user.py
├─ blog.py

---

## How authentication works (JWT)

1. **Login** via `POST /login` using form fields `username` (email) and `password`.
2. The server checks the user in the database and verifies the hashed password.
3. On success it returns a JSON with:
   ```json
   { "access_token": "...", "token_type": "bearer" }
4. For protected routes, send the token in the Authorization header:
- Authorization: Bearer <access_token>
- In this codebase, most user and blog routes are protected by the get_current_user dependency from oaut2.py.

---

## Routes exposed by the existing code
- Paths and names below reflect your current router files. (If you change them in code later, adjust this list accordingly.)

---

## Authentication
- POST /login → returns JWT access token (form-encoded: username, password)

---

## Users (in routers/user.py)
- POST /user/create → create a new user (body: name, email, password)
- GET /user/get/{id} → fetch a user by id
- DELETE /user/delete/all → delete all users

## Blogs (in routers/blog.py)
- GET /blog/get → list all blogs
- GET /blog/get/{id} → get a blog by id
- POST /blog/create → create a blog (body: title, body)
- PUT /blog/update/{id} → update a blog
- DELETE /blog/delete/{id} → delete a blog

---

## Running the server
1) Install dependencies: pip install -r requirements.txt
2) Start the API: uvicorn blog.main:app --reload (The app will create the SQLite DB (if missing) and the tables via models.Base.metadata.create_all(...)). Open http://127.0.0.1:8000/docs to interact with the API.

---

## Example workflow (using curl)
- If your POST /user/create is open, create a user first;
- if it’s protected, seed a user in the DB beforehand (or use the Swagger UI if you’ve already got a token).

---

## Tech stack
- FastAPI (web framework)
- Uvicorn (ASGI server)
- SQLAlchemy (ORM)
- Passlib[bcrypt] (password hashing)
- python-jose (JWT)
- SQLite (development database)

## Author
- Developed by Nicolas Constantinou
- 2025
