from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserOut

def create_user(user: UserCreate, db: Session):
    db_user = User(**user.model_dump)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserOut.model_validate(db_user)

def get_user_by_id(user_id: int, db: Session):
    return UserOut.model_validate(db.query(User).filter(User.id == user_id).first())

def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return [UserOut.model_validate(user) for user in db.query(User).offset(skip).limit(limit).all()]

# def get_user_by_username(username: str, db: Session):
#     return db.query(User).filter(User.username == username).first()

# def update_user(user_id: int, user: UserUpdate, db: Session):
#     db_user = get_user_by_id(user_id, db)
#     if not db_user:
#         return None
#     for key, value in user.model_dump().items():
#         setattr(db_user, key, value)
#     db.commit()
#     db.refresh(db_user)
#     return db_user