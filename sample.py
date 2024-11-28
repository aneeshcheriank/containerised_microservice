from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("add/{num1}/{num2}")
async def add(num1: int, num2:int):
    """Add two numbers tougther"""
    sum =  num1+num2
    return {"total": sum}