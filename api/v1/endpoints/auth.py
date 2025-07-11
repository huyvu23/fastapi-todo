from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from schemas import UserRead,UserLogin
from db.deps import get_db
from services import verify_user_login

router = APIRouter()

@router.post("/login",response_model=UserRead)
def login(information_login:UserLogin, db:Session = Depends(get_db)):
    return verify_user_login(db,information_login)
