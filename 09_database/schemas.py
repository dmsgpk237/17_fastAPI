# 스키마는 데이터베이스에 있는 모델을 보여줌, 기본 타입을 지정할 수 있음.

from pydantic import BaseModel
from typing_extensions import Optional

# request를 받거나, response를 받을 때 사용하는 기본 모델
# 기본 형식을 만들어 놓을 수 있다.

class TeacherBase(BaseModel):
    name : str
    is_active : bool
    nickname : Optional[str] = None
    description : Optional[str] = None
    
# SqlAlchemy 모델 : 데이터베이스 통신을 위한 데이터 구조정의
# Pydantic 모델 : API 요청과 응답을 위한 데이터 구조정의
    
#  request 요청 모델
class TeacherCreate(TeacherBase):
    pass

# response 응답 모델
class TeacherResponse(TeacherBase):
    
    # 추가로 전달해줄 필요한 값을 넣음
    id : int

# 업데이트할 때 사용되는 모델
class TeacherUpdate(BaseModel):
    name : Optional[str] = None
    is_active : Optional[bool] = None
    nickname : Optional[str] = None
    description : Optional[str] = None
    
    
# ------------------------------------------------------------------------------------------------

class StudentBase(BaseModel):
    name : str
    nickname : Optional[str] = None
    launch_menu : str
    description : Optional[str] = None
    
# request 요청 모델
class StudentRequest(StudentBase):
    pass

# response 응답 모델
class StudentResponse(StudentBase):
    id : int

# update
class StudentUpdate(StudentBase):
    pass