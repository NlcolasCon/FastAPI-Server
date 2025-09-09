from fastapi import status, HTTPException, Depends
from ... import models, schemas, hashing
from sqlalchemy.orm import Session

def create_user(request:schemas.User, db:Session):
    blog = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def get_user(id:int, db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    return user

def delete_user_all(db:Session):
    db.query(models.User).delete(synchronize_session=False)
    db.commit()
    return "DELETED ALL BLOGS AVAILABLE"