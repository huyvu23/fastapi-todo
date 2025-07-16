from fastapi import APIRouter
from schemas import UserLogin,UserCreate,InformationUserLogin,UserRead
from services import verify_user_login,create_user
from db.deps import SessionDep

router = APIRouter()

@router.post("/register",response_model=UserRead)
def register_user(user: UserCreate,db: SessionDep):
    return create_user(user,db)

@router.post("/login",response_model=InformationUserLogin)
def login(information_login:UserLogin, db:SessionDep):
    return verify_user_login(db,information_login)
