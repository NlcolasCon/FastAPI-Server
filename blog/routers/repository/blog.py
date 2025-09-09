from fastapi import status, Response, HTTPException, Depends
from ... import models, schemas
from typing import List
from sqlalchemy.orm import Session

def get_blog(id:int, response:Response, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Not available")
    #  OR:
    #   response.status_code = status.HTTP_404_NOT_FOUND
    #   return {'details':f"Blog with id {id} is not available"}
    return blog

def get_blog_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create_blog(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title,body=request.body,user_id=1)     ##hardcoded user_id for now
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)   
    return new_blog 

def delete_blog(id:int, response:Response, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    if not blog:
        raise HTTPException(status_code=404, detail="Not available")
    return "DELETED"

def delete_blog_all(db: Session):
    db.query(models.Blog).delete(synchronize_session=False)
    db.commit()
    return "DELETED ALL BLOGS AVAILABLE"

def update_blog(id:int, request:schemas.Blog, db:Session):
    blog =  db.query(models.Blog).filter(models.Blog.id == id).update({'title':request.title, 'body':request.body})
    db.commit()
    if not blog:
        raise HTTPException(status_code=404, detail="Not available")
    return request