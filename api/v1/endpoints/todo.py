from fastapi import APIRouter
from schemas import TodoCreate,TodoResponse
from services import create_new_todo,get_all_todo as get_all_todo_service

router = APIRouter()

@router.post('/',response_model=TodoResponse)
def create_todo(todo:TodoCreate):
    return create_new_todo(todo)

@router.get('/',response_model=list[TodoResponse])
def get_all_todo():
    return get_all_todo_service()


