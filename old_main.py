from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: int | None = None
    
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id":1}, {"title":"Favorite food", "content":"i like pizza", "id":2}]


def find_post(id):
    for i in my_posts:
        if i['id'] == id:
            return i


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
        
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts(post:Post):
        return {"data":post}
        print(posts)
        
# @app.post("/createposts") not best practice, use plural and specific terms
@app.post("/posts", status_code = status.HTTP_201_CREATED)
def create_post(post: Post, response: Response):
    # return {"message":"Successfully created posts"}
    # return {"new_post" : f"title: {payload['title']} content: {payload['content']}"}
# two things that we want from the user::     Title: str, Content: str, we could also include
# category of the post, numbers, booleans if its published or not and shitssss
    print(post.dict()) 
    response.status_code = status.HTTP_201_CREATED
    
    # Commenting old code to create new posts from database
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    
@app.get('/posts/{id}')
def get_post(id: int, response: Response):
    
    # post = find_post(int(id)) converting to string is no longer needed as you can convert from function "get_post"
    
    post = find_post(id)
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message':f"message with the id: {id} was not found"}
        # Standard way of doing it
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= f"message with the id: {id} was not found")

    # print(post)
    return {"Post detail": post}

@app.delete('/posts/{id}', status_code= status.HTTP_204_NO_CONTENT)
def delete_post(id: int, response: Response):
    #  Deleting a post
    # First step is to find the index of an array that has the required ID
    #  my_posts.pop(index)     that is the syntax
    
    index = find_index_post(id)
    
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= f"Post with the id: {id} does not exist.")
        
    
    my_posts.pop(index)
    return {'message':'The post was succesfully deleted'}
    return Response(status_code = status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= f"Post with the id: {id} does not exist.")
    
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"message":"Post has been updated successfully."}
    return {'data': post_dict}