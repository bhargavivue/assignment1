
from fastapi import FastAPI, HTTPException
from app.model.OperationInput import OperationInput 

app = FastAPI(title="Simple Calculator API")

# Add two numbers
@app.post("/add/")
async def add(input: OperationInput):
    result = input.number1 + input.number2
    return {
        "operation": "addition",
        "number1": input.number1,
        "number2": input.number2,
        "result": result
    }

# Subtract two numbers
@app.post("/subtract/")
async def subtract(input: OperationInput):
    result = input.number1 - input.number2
    return {
        "operation": "subtraction",
        "number1": input.number1,
        "number2": input.number2,
        "result": result
    }

# Multiply two numbers
@app.post("/multiply/")
async def multiply(input: OperationInput):
    result = input.number1 * input.number2
    return {
        "operation": "multiplication",
        "number1": input.number1,
        "number2": input.number2,
        "result": result
    }

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Simple Calculator API!"}



    