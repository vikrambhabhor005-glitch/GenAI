from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

exp=[]
id=1

class Expenses(BaseModel):
    
    expense_name: str
    expense_type: str
    expense_description: str
    expense_price: float
    expense_payment_type: str

@app.post("/expenses/")
def create_exepense(expense:Expenses):
    global id
    new_expense = expense.dict()
    new_expense["expense_id"] = id
    new_expense["is_deleted"]= False
    exp.append(new_expense)
    id +=1
    return {
        "msg" : "New expenses added sucessfully",
        "data" : exp
    }

@app.get("/expenses")
def get_exepense():
    return {
        "msg":" New Expenses get sucessfully",
        "data": exp
    }

@app.get("/expensesbyId/{expense_id}")
def get_expenses_by_id(expense_id : int):
    for i in exp:
        if i["expense_id"] == expense_id:
            return { 
                "msg" : "Expenses are fached sucessfully",
                "data" : i

            }

@app.put("/expensesupdatebyId/{expense_id}")
def update_expense(expense_id : int , updated_expenses: Expenses ):
    for j in exp:
        if j["expense_id"] == expense_id:
            j["expense_id"] =  updated_expenses.expense_id
            j["expense_name"] = updated_expenses.expense_name 
            j["expense_type"] = updated_expenses.expense_type
            j["expense_description"] =updated_expenses.expense_description
            j["expense_price"] = updated_expenses.expense_price
            j["expense_payment_type"] = updated_expenses.expense_payment_type
        return {
        "msg":"expenses updated sucessfully",
        "data": j
    }
    return{
        "msg":"No data found"
    }
    
@app.delete("/expensesdeletedbyId/{expenses_id}")
def delete_expense():
    exp.clear()
    return {
        "msg":"all xpense deleted sucessfully",
        "data" : exp
    }
