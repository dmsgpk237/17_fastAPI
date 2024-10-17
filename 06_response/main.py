from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# 응답
# response_model을 사용해서 응답 타입을 선언할 수 있다.
# 자동 검증 : 응답 데이터가 지정된 모델과 일치하는지 검증
# 자동 변환 : 응답 데이터를 지정된 모델의 형식으로 변환
# 문서화 : API 문서에 응답 데이터의 구조가 명확히 표시됨.

class Teacher(BaseModel):
    name: str
    teacher_id: int
    nickname: str
    
@app.get("/teachers/{teacher_id}", response_model=Teacher)
async def get_teacher(teacher_id:int):
    
    # 서비스 로직을 통해 return 형태를 객체형태로 만들고
    # teacher = Teacher(
    #     name = "태근",
    #     teacher_id = teacher_id,
    #     nickname="bear"
    # )
    
    return {
        "name" : "태근",
        "teacher_id" : teacher_id,
        "nickname" : "bear"
    }