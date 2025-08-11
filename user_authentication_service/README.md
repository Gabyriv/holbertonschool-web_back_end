# User Authentication Service

Simple session-based authentication service built with Flask, SQLAlchemy, and bcrypt.

This project demonstrates a minimal auth flow:

1. Register users
2. Log in and create sessions (cookie-based)
3. View profile via session
4. Log out (destroy session)
5. Request password reset token
6. Update password using reset token

## Requirements

- Python 3.9 (project targets Ubuntu 20.04 LTS / python3.9)
- SQLite (via SQLAlchemy)

Python packages:

- Flask
- SQLAlchemy
- bcrypt
- pycodestyle (for style checks)

## Setup

Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

Start the Flask app:

```bash
python3 app.py
```

Server runs at [http://0.0.0.0:5000](http://0.0.0.0:5000)

## Database

- SQLite file `a.db` is created in the project directory.
- Tables are created via SQLAlchemy on app start (see `db.py`, `user.py`).

## Project Structure

- `app.py` — Flask HTTP API; only interacts with `Auth` (never `DB` directly).
- `auth.py` — Authentication logic and orchestration using `DB` public methods.
- `db.py` — SQLAlchemy session and DB access layer (`add_user`, `find_user_by`, `update_user`).
- `user.py` — SQLAlchemy `User` model (`email`, `hashed_password`, `session_id`, `reset_token`).
- `main.py` — Simple script to exercise core `Auth` features (optional).

## API

All endpoints use `application/x-www-form-urlencoded` form data unless noted.

1. Register user

- POST `/users`
- Form: `email`, `password`
- 200: `{ "email": "<email>", "message": "user created" }`
- 400: `{ "message": "email already registered" }`

Example:

```bash
curl -XPOST localhost:5000/users \
  -d 'email=bob@bob.com' -d 'password=mySuperPwd'
```

2. Login (create session)

- POST `/sessions`
- Form: `email`, `password`
- 200: Set-Cookie `session_id=<uuid>`; body `{ "email": "<email>", "message": "logged in" }`
- 401 on invalid credentials

Example:

```bash
curl -XPOST localhost:5000/sessions \
  -d 'email=bob@bob.com' -d 'password=mySuperPwd' -v
```

3. Profile (requires session cookie)

- GET `/profile`
- Cookie: `session_id`
- 200: `{ "email": "<email>" }`
- 403 if session invalid

Example:

```bash
curl -XGET localhost:5000/profile -b "session_id=<uuid>"
```

4. Logout (destroy session)

- DELETE `/sessions`
- Cookie: `session_id`
- 302 redirect to `/` on success; 403 if no valid session

Example:

```bash
curl -XDELETE localhost:5000/sessions -b "session_id=<uuid>" -v
```

5. Request password reset token

- POST `/reset_password`
- Form: `email`
- 200: `{ "email": "<email>", "reset_token": "<uuid>" }`
- 403 if email not registered

Example:

```bash
curl -XPOST localhost:5000/reset_password -d 'email=bob@bob.com'
```

6. Update password with reset token

- PUT `/reset_password`
- Form: `email`, `reset_token`, `new_password`
- 200: `{ "email": "<email>", "message": "Password updated" }`
- 403 if token invalid or required fields missing

Example:

```bash
curl -XPUT localhost:5000/reset_password \
  -d 'email=bob@bob.com' \
  -d 'reset_token=<uuid>' \
  -d 'new_password=NewStrongPwd1!'
```

## Style and Conventions

- Files are executable and start with `#!/usr/bin/env python3`.
- Code follows `pycodestyle` 2.5.
- All modules, classes, and functions include docstrings.
- All functions are type-annotated.
- Flask app only uses `Auth` (not `DB` directly). Outside `Auth`/`DB`, only public methods are used.

## Notes

- Do not store plaintext passwords. We use `bcrypt` to hash passwords.
- Sessions are simple UUIDs stored in the `users.session_id` column and set as a cookie.
