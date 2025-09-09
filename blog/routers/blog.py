from fastapi import APIRouter   #ksmsvsmkvmsdkmvsd
from fastapi import status, Response, HTTPException, Depends
from .. import schemas, database, models, oaut2
from typing import List
from sqlalchemy.orm import Session
from .repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blog API']

) #kmsfkmdmkdsmkfsdmfksdom

#Get BLOG FROM DATABASE
@router.get('/get/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def getID(id:int, response:Response, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.get_blog(id, response, db)

#GET ALL BLOGS FROM DATABASE
@router.get('/get', response_model=list[schemas.Blog])#to get a response model of ShowBlog objects, but there are a lot of them => list of objects
def get_all(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.get_blog_all(db)

#PUT BLOG IN DATABASE
@router.post('/post', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.create_blog(request, db)

#DELETE FROM DATABASE
@router.delete('/delete/{id:int}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id:int, response:Response, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.delete_blog(id, response, db)

#DELETE ALL BLOGS FROM DATABASE
@router.delete('/delete/all')
def deleteAllBlogs(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.delete_blog_all(db)

#UPDATE FROM DATABASES
@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.update_blog(id,request,db)

