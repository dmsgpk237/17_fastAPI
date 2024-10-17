from fastapi import FastAPI, APIRouter
from routers import student_router, teacher_router
app = FastAPI()

# Router를 사용하는 이유
# 모듈화
# 재사용성
# 네임 스페이스 관리
# 미들웨어 및 이벤트 핸들러


# fastapi 패키지 구조

# 1. models
#   Database 저장될 데이터 형식같은 class를 저장한다.
#   ORM을 사용할 때

# 2. routers
#   api의 andpoint 관련 패키지

# 3. servieces
#   비즈니스 로직을 처리 관련 패키지

# 4. shcemas
#   Pydantic 모델 정의 (검증 및 직렬화) 관련 패키지

# 5. dependencies
#   의존성 주입을 위한 모듈 (ex. database)

router = APIRouter()

app.include_router(router)
app.include_router(student_router.student)
app.include_router(teacher_router.teacher)

@app.get("/")
async def root():
    return {"message" : "Hello FastAPI"}

