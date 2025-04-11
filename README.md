

# Swift Tasks

**Swift Tasks** is a smart and minimal task management API powered by Django and Django REST Framework. It allows users to register, authenticate using JWT, create tasks, and benefit from automatic smart ranking based on urgency, deadline, and importance. This project was built as a capstone for the ALX Software Engineering Backend program.

---

## Features

- **User Registration & Authentication** (JWT-based)
- **Create, Read, Update, Delete Tasks**
- **Smart Task Ranking Algorithm**:
  - Ranks tasks dynamically based on their priority, urgency, and deadlines.
- **Background Task Support** for ranking using `django-background-tasks`
- **Secure API endpoints** with CORS and JWT protection

---

## API Endpoints

| Endpoint               | Method | Description                      |
|------------------------|--------|----------------------------------|
| `/api/register/`       | POST   | User registration                |
| `/api/token/`          | POST   | Obtain JWT access & refresh      |
| `/api/token/refresh/`  | POST   | Refresh access token             |
| `/api/tasks/`          | GET/POST | List or create tasks           |
| `/api/tasks/<id>/`     | GET/PUT/DELETE | View, update, or delete a task |
| `/api/tasks/smart-rank/` | GET | View all tasks, smartly ranked |

---

## Models

### User
- Inherits Django’s default `AbstractUser` model.

### Task
- `title`: CharField
- `description`: TextField
- `priority`: IntegerField (1-5)
- `deadline`: DateTimeField
- `completed`: BooleanField
- `created_at`: DateTimeField (auto)
- `owner`: ForeignKey (User)

---

## Tech Stack

- Python & Django
- Django REST Framework
- JWT Authentication (`djangorestframework-simplejwt`)
- Background Processing (`django-background-tasks`)
- CORS Handling (`django-cors-headers`)

---

## Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/your-username/swift-tasks.git
cd swift-tasks