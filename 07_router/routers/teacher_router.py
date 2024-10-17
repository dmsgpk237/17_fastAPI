from fastapi import APIRouter

student = APIRouter(
    prefix="/api/teachers", # 고정 경로
    tags=["teachers"],
    
    
)

@student.get("/")
async def geet_teachers():
    return {"message" : "교사입니다."}