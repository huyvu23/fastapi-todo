
from models.user import User
from sqlalchemy.orm import Session

# Encapsulates business logic and interacts with the database.
def create_user(user_data):
    return {"id":1,"email":user_data.email}

def get_users(db:Session):
    try:
        users = db.query(User).all()
        if len(users):
            return users
        return []
    except Exception as e:
        print('e:',e)