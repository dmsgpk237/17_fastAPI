from fastapi import APIRouter

student = APIRouter(
    prefix="/api/students", # 고정 경로
    tags=["students"],
    
    
)

@student.get("/")
async def geet_student():
    return {"message" : "학생입니다."}