from pydantic import BaseModel
from datetime import date

class ExpenseCreate(BaseModel):
    amount: float
    category: str
    date: date

class ExpenseOut(ExpenseCreate):
    id: int

    class Config:
        orm_mode = True
