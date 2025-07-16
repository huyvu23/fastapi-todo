from sqlalchemy.orm import Session
from models import Todo
from schemas import TodoResponse,TodoCreate
from fastapi import HTTPException,status

def create_new_todo(todo_data:TodoCreate,db:Session,user_id:int) -> TodoResponse:
    try:
        new_todo = Todo(
            title=todo_data.title,
            description=todo_data.description,
            user_id=user_id 
        )
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)
        return new_todo
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

def get_all_todo(db:Session,current_user_id:int):
    try:
        todos = db.query(Todo).filter(Todo.user_id == current_user_id).all()
        if len(todos):
            return todos
        return []
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
    