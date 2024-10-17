from fastapi import FastAPI

app = FastAPI()

# 경로 매개변수
# 웹 어플리케이션에서 URL 경로의 일부로 사용된다.
# 보통 클라이언트에서 서버에 요청할 때 특정 자원을 식별하는데 사용되는 값

@app.get('/items/{item_id}')
async def read_item(item_id):
    return {"item_id": item_id}

# 타입이 있는 매개변수
# 파이썬 표준 타입을 사용할 수 있다.

@app.get('/items/type/{item_id}')
async def read_item_type(item_id: int):
    return {"item_id" : item_id}


# Enum으로 매개변수 받기
from enum import Enum
class Teachers(str, Enum):
    kamja = "감자"
    gorilla = "고릴라"
    bear = "깜지곰"
    
@app.get("/teacher/{teacher_name}")
async def get_teacher(teacher_name: Teachers):
    
    if teacher_name is Teachers.bear:
        return {"우리반 선생님은 깜지곰입니다."}
    elif teacher_name is Teachers.gorilla:
        return {"우리반 선생님은 고릴라입니다."}
    
    return {"우리반 선생님은 감자입니다."}

# fastAPI 작성시 주의사항
# 순서문제
# api의 경로 동작은 순차적으로 실행되기 때문에 중복되는 url을 작성할 경우
# 작은 범위의 경로를 상단에 적는 것이 좋다.

@app.get("/users/me")
async def read_me():
    return {"user_id": "user_me"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

