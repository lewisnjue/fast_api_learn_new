from fastapi import FastAPI, Response,status
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
app = FastAPI()

# this define the path operation

class Post(BaseModel):
    title: str
    content: str
    id:int = randrange(1,1000000)


my_posts = [
    {"title":"title of post 1",
     "content":"content of post 1",
     "id":1},
     {
         "title":"favoraite foods",
         "content":"i like pizza",
         "id":2
     }

]


def find_post(id):
    post = ''
    for p in my_posts:
        if p['id'] == id:
            post = p 
            break
        else:
            continue

    return post 
    




@app.get("/") 
def root():
    return {"messange":"hello world"}


@app.get('/posts') 
def get_posts():
    return {"data":my_posts}


@app.post('/posts')
def create_post(post:Post):
    mypost = post.model_dump()
    my_posts.append(mypost)
    return {"post":mypost}

@app.get('/posts/{id}')
def get_post(id:int,response:Response):
    search_post = find_post(id)
    if not search_post:
        response.status_code = status.HTTP_404_NOT_FOUND

    return {'messange':search_post}
    


# to run your server for development you will run the follwong code:
# uvicorn main:app -> note main is the name of the python file and app is the 
# name of the instance of our FastApi

