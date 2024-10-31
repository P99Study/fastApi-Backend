# app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World v5 final from Docker"}

origins = [
    "http://localhost:3000",  # Local development
    os.getenv("FRONTEND_URL")  # Dynamic URL for deployed frontend
]

# Allow requests from localhost (React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Update with React frontend URL if deployed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/data")
async def get_data():
    frontend_url = os.getenv("FRONTEND_URL")
    print(f"Frontend url is {frontend_url}")
    return {"message": "Hello from FastAPI Backend v5 dynamic final!"}

# Define a Pydantic model for request body
class DataRequest(BaseModel):
    person: str = "Rohin"

@app.post("/api/data")
async def post_data(data: DataRequest):
    print(f"Origins is {origins}")
    return {"message": f"Hello from FastAPI to {data.person} Backend v5!"}