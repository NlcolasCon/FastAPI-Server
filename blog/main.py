from fastapi import FastAPI, Depends
from . import schemas, models, hashing
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from fastapi import status, Response, HTTPException
from typing import List
from .hashing import Hash
from .routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(blog.router) #dskmvksnkjlvnsdklnjkdsnkb;l
app.include_router(authentication.router)












#############################################
#API WITHOUT ROUTES AND REPOSITORIES:       #
#############################################
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# #PUT BLOG IN DATABASE
# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['Blog'])
# def post(request: schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title,body=request.body,user_id=1)     ##hardcoded user_id for now
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)   
#     return new_blog 

# #GET ALL BLOCKS FROM DATABASE
# @app.get('/blog', response_model=list[schemas.Blog], tags=['Blog'])#to get a response model of ShowBlog objects, but there are a lot of them => list of objects
# def getAll(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# #GET BLOCKS FROM DATABASE USING FILTERS
# # @app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog, tags=['Blog'])
# # def getID(id:int, response:Response, db: Session = Depends(get_db)):
# #     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
# #     if not blog:
# #         raise HTTPException(status_code=404, detail="Not available")
# #     #  OR:
# #     #   response.status_code = status.HTTP_404_NOT_FOUND
# #     #   return {'details':f"Blog with id {id} is not available"}
# #     return blog

# #DELETE FROM DATABASE
# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Blog'])
# def delete(id:int, response:Response, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).delete(synchronize_session=False)
#     db.commit()
#     if not blog:
#         raise HTTPException(status_code=404, detail="Not available")
#     return "DELETED"

# @app.delete('/blog/delete/all', tags=['Blog'])
# def deleteAllBlogs(db: Session = Depends(get_db)):
#     db.query(models.Blog).delete(synchronize_session=False)
#     db.commit()
#     return "DELETED ALL BLOGS AVAILABLE"

# #UPDATE FROM DATABASES
# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['Blog'])
# def update(id:int, request: schemas.Blog, db: Session = Depends(get_db)):
#     blog =  db.query(models.Blog).filter(models.Blog.id == id).update({'title':request.title, 'body':request.body})
#     db.commit()
#     if not blog:
#         raise HTTPException(status_code=404, detail="Not available")
#     return request

# #CREATE A USER IN DATABASE
# @app.post('/user', response_model=schemas.ShowUser, tags=['User'])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     blog = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
#     db.add(blog)
#     db.commit()
#     db.refresh(blog)
#     return blog

# #GET A USER FROM DATABASE
# @app.get('/user/{id}', response_model=schemas.ShowUser, tags=['User'])
# def get_user(id:int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
#     return user

# #DELETE ALL USERS FROM DATABASE
# @app.delete('/user/delete/all', tags=['User'])
# def deleteAllUsers(db: Session = Depends(get_db)):
    # db.query(models.User).delete(synchronize_session=False)
    # db.commit()
    # return "DELETED ALL BLOGS AVAILABLE"