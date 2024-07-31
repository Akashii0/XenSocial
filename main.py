from fastapi import FastAPI
# import models
# from database import engine
from routers import post, user, auth, vote
# from config import settings
from fastapi.middleware.cors import CORSMiddleware

# print(settings.database_password)

# models.Base.metadata.create_all(bind=engine)


#  Declaring an Instance 
app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id":1}, {"title":"Favorite food", "content":"i like pizza", "id":2}]

# Hard coded way, before using databases
# def find_post(id):
#     for i in my_posts:
#         if i['id'] == id:
#             return i

# Hard coded way, before using databases
# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i
    
    
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# Path Operation
# Request Get Method URL : "/"
@app.get("/")
async def root():
    return {"message": "Hello World"}



    
    
    