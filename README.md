### PowerCred Assignment [Full Stack]
---
<!-- Table -->
**Description:**
The objective of this assignment is to demonstrate my proficiency as a full-stack developer with expertise in using FastAPI for the backend and React for the frontend. I am required to build a more advanced application that allows users to manage a list of tasks with additional features.

### Steps To Run Backend

- `git clone https://github.com/Jiya-Ull-Haq/power_ca_backend`,
- `cd power_ca_backend`
- `python3 -m venv venv`,
- `source ./venv/bin/activate`,
- `pip3 install -r requirements.txt`,
- `uvicorn main:app --reload`

### Technologies Used

- `Python, FastAPI (Backend Framework)`,
- `SQLite3 (Sql database)` (Automatic Migration, Code First Approach)

- `sqlalchemy for ORM`,
- `JWT for securing API endpoints`

### Folder Structure

- app
  - controllers.py
  - models.py
  - database.py
  - schemas.py
- main.py
- pca.db


### API END POINTS

| Request | URL               | Description           |
| -       | -                 | -                     |
| (POST)  | /login            | Logs in a user.       |
| (POST)  | /register         | Registers a new user. |
| (POST)  | /create-task      | Creates a new task.   |
| (GET)   | /get-tasks        | Gets all tasks.       |
| (PUT)   | /update-task      | Updates a task.       |
| (GET)   | /get-users        | Gets all users.       |
