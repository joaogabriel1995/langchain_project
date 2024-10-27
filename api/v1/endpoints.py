from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter()

class InputRequest(BaseModel):
    question: str

@router.get("/hello-word")
async def generate_response():
    return {"response": "hello-word"}