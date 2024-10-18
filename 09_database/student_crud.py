from sqlalchemy.orm import Session
import schemas, models
from fastapi import HTTPException

# student 생성
def create_student(db : Session, student = schemas.StudentRequest):
    
    db_student = models.Student(
        name = student.name,
        nickname = student.nickname,
        launch_menu = student.launch_menu,
        description = student.description
    )
    
    db.add(db_student)
    
    db.commit()
    
    return db_student


# student 단일 조회
def get_student_by_id(db: Session, student_id: int):
    found_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    
    return found_student   


# student 전체 조회
def get_all_student(db: Session):
    all_student = db.query(models.Student).all()
    
    return all_student

# student 수정
def update_student(db: Session, student_id: int, student:schemas.StudentUpdate):
    
    found_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    
    if found_student is None:
        raise HTTPException(status_code=404, detail="학생을 찾을 수 없습니다.")
    
    if student.name is not None:
        found_student.name = student.name
        
    if student.nickname is not None:
        found_student.nickname = student.nickname
        
    if student.launch_menu is not None:
        found_student.launch_menu = student.launch_menu
        
    if student.description is not None:
        found_student.description = student.description
        
    db.commit()
    
    return found_student


# student 삭제
def delete_student(db: Session, student_id: int):
    found_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    
    if found_student is None:
        raise HTTPException(status_code=404, detail="학생을 찾을 수 없습니다.")
    db.delete(found_student)
    
    db.commit()
