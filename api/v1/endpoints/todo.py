from fastapi import APIRouter,Request
from schemas import TodoCreate,TodoResponse
from services import create_new_todo,get_all_todo as get_all_todo_service
from db.deps import SessionDep

router = APIRouter()

@router.post('/',response_model=TodoResponse)
def create_todo(request:Request, todo:TodoCreate,db: SessionDep):
    user = getattr(request.state, "user", None)
    return create_new_todo(todo,db,user["id"])

@router.get('/',response_model=list[TodoResponse])
def get_all_todo(request:Request,  db: SessionDep):
    user = getattr(request.state, "user", None)
    return get_all_todo_service(db,user["id"])


