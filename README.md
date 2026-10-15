# Student Management API

## About the Project

This project is a simple student management system built using Python, FastAPI, and SQLite. It provides API endpoints to add, view, update, and delete student records.

## Features

- Add a new student
- View all students
- Search for a student by ID
- Filter students by course
- Update student details
- Delete student records
- Validate request data
- Handle missing students and duplicate email addresses

## Technologies Used

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic

## Setup

1. Clone the repository.
2. Open the project folder in the terminal.
3. Create and activate a virtual environment.
4. Install the required packages:

   `python -m pip install -r requirements.txt`

5. Start the server:

   `python -m uvicorn app.main:app --reload`

6. Open `http://127.0.0.1:8000/docs` to test the API.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/students` | Create a student |
| GET | `/students` | Get all students |
| GET | `/students/{student_id}` | Get a student by ID |
| PATCH | `/students/{student_id}` | Update a student |
| DELETE | `/students/{student_id}` | Delete a student |

## Database

The application uses SQLite. The `students.db` database file is created automatically when the application starts.

## Testing

The API can be tested through the interactive Swagger interface at `/docs`.

## Future Improvements

- Add student search by name
- Add pagination
- Add a simple frontend interface