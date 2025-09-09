from pydantic import BaseModel
from typing import List, Optional

class Blog(BaseModel):
    title:str
    body:str

class ShowUser(BaseModel):
    name:str
    email:str
    blog : List[Blog]
    class Config():
        from_attributes=True
        
class ShowBlog(BaseModel):
    title:str
    body:str
    user:ShowUser
    #or command: pass, to get all attributes passed from Blog to this class if it has (Blog) for inheritance
    class Config():
        from_attributes=True

class User(BaseModel):
    name:str
    email:str
    password:str

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    username: Optional[str] = None


