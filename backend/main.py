from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import SessionLocal, engine, Base
from .models import Expense
from .schemas import ExpenseCreate, ExpenseOut
from .insights import calculate_insights

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="FinSight API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/expenses", response_model=ExpenseOut)
def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    new_expense = Expense(
        amount=expense.amount,
        category=expense.category,
        date=expense.date
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

@app.get("/expenses", response_model=list[ExpenseOut])
def list_expenses(db: Session = Depends(get_db)):
    return db.query(Expense).all()

@app.get("/insights")
def get_insights(db: Session = Depends(get_db)):
    expenses = db.query(Expense).all()
    return calculate_insights(expenses)

@app.get("/")
def root():
    return {"status": "FinSight API running"}
