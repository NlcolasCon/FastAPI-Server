from fastapi import APIRouter   #ksmsvsmkvmsdkmvsd
from fastapi import Depends
from .. import schemas, database, oaut2
from sqlalchemy.orm import Session
from .repository import user

router = APIRouter(
    prefix="/user",
    tags=['User API']
)

#CREATE A USER IN DATABASE
@router.post('/create', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oaut2.get_current_user)):
    return user.create_user(request, db)

#GET A USER FROM DATABASE
@router.get('/get/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oaut2.get_current_user)):
    return user.get_user(id, db)

#DELETE ALL USERS FROM DATABASE
@router.delete('/delete/all')
def deleteAllUsers(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oaut2.get_current_user)):
    return user.delete_user_all(db)