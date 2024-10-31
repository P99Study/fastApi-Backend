# app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World v5 final from Docker"}

# Allow requests from localhost (React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Local development
        "http://54.242.218.109"  # New origin for deployed React frontend
    ],  # Update with React frontend URL if deployed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/data")
async def get_data():
    return {"message": "Hello from FastAPI Backend v4 final!"}

# Define a Pydantic model for request body
class DataRequest(BaseModel):
    person: str = "Rohin"

@app.post("/api/data")
async def post_data(data: DataRequest):
    return {"message": f"Hello from FastAPI to {data.person} Backend v5!"}