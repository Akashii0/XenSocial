from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional
from typing_extensions import Annotated

from pydantic import BaseModel, Field

# from pydantic.types import conint    oldddd
# Creating a format for the database, declaring valid data for the user 
# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
    # rating: int | None = None
    
# class CreatePost(BaseModel):
#     title: str
#     content: str
#     published: bool = True

    
# class UpdatePost(BaseModel):
#     title: str
#     content: str
#     published: bool 

# To avoid creating too much posts, easy way out is:
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True
 
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
    
class PostCreate(PostBase):
    pass
    
    
# class for the response, us sending data to the user
# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool
#     created_at: datetime
    
#     class Config:
#         orm_mode = True
# to make it faster, if you want to inherit from existing pydantic model,
# use it instead of Basemodel. i.e use Postbase instead of BaseModel


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    
    class Config:
        orm_mode = True
        
    
class PostOut(BaseModel):
    Post: Post
    Votes: int
    
    class Config:
        orm_mode = True
    
# Setting up a schema for the token

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None
    # id: str | None = None
    

class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(le=1)]
    # dir: conint(le=1)
    
    # less than or equal to one, problem is that, it allows negative
    
# class PostUpdate(PostBase):
#     pass