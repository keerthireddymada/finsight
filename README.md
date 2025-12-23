# FinSight – Full-Stack Expense Tracking & Insights Application

FinSight is a full-stack web application for tracking expenses and generating data-driven spending insights.  
The project focuses on backend API design, database integration, frontend-backend communication, and clear, explainable business logic rather than UI-heavy frameworks.

---

## 🚀 Features

- Add and view expenses
- Categorize expenses
- Backend analytics to detect overspending
- RESTful APIs built with FastAPI
- Lightweight frontend using HTML, CSS, and Vanilla JavaScript
- Interactive API documentation via Swagger UI

---

## 🛠 Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

### Frontend
- HTML
- CSS
- Vanilla JavaScript (Fetch API)

---

## ▶️ How to Run FinSight

```bash
git clone https://github.com/keerthireddymada/finsight.git
cd finsight

python -m venv .venv

.venv\Scripts\Activate
# source .venv/bin/activate  (macOS/Linux)

pip install fastapi uvicorn sqlalchemy pydantic

uvicorn backend.main:app --reload

```
Backend URL:

http://127.0.0.1:8000


Swagger UI:

http://127.0.0.1:8000/docs


Frontend:

Open frontend/index.html in a browser

---

## 🔌 API Endpoints
POST /expenses

Add a new expense

{
  "amount": 500,
  "category": "Food",
  "date": "2025-01-01"
}

GET /expenses

Retrieve all stored expenses

GET /insights

Retrieve spending analytics and overspending detection

All endpoints are documented and testable via Swagger UI.

---

## 🧠 Spending Insights Logic

Category Total: 
A category total is the sum of all expenses belonging to the same category.

Example:

Food    → 200 + 300 = 500
Travel  → 1000

### Overspending Detection Logic

Steps:

Group expenses by category

Calculate category totals

Compute average spending across categories

Flag overspending categories

Rule:

category_total > average_spend × 1.2


### Why this approach:

- Simple and explainable

- Works well with small datasets

- Avoids black-box or fake ML claims

- Easy to extend to advanced analytics later

All analytics logic is implemented on the backend.

---

## 📁 Project Structure

finsight/

├── backend/

│   ├── main.py

│   ├── database.py

│   ├── models.py

│   ├── schemas.py

│   └── insights.py

├── frontend/

│   ├── index.html

│   ├── style.css

│   └── app.js

├── README.md

└── .gitignore

---

## 🎯 Project Purpose

This project demonstrates:

Full-stack development fundamentals

RESTful API design

Database-backed persistence

Frontend-backend integration

Explainable business logic

Real-world debugging experience
