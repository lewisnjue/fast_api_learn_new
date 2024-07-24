#FAST API 
the first thing that you will need to do is to install all the dependancies using the following command
```sh
pip install fastapi
```
after this create main.py file and the first code write the following 
```py
from fastapi import FastApi

app = FastApi()

@app.get('/')
def hello():
    return {"messange":'hello world'}

```
after this you can start your development server with the following command 
```sh
uvicorn main:app --reload
```
the reload flag make sure that the webseerver reload whenver 
a change occur in your code

if the method used is post and you want to access the body that is passed  you will do the following in your code

```py
from fastapi.params import Body

@app.post('/createposts')
def create_post(payload:dict = Body(...)):
    print(payload)
    return {"messange":"you created a post"}
```
in this case im extracting the body and converting it to dict 
then assign the dict to a variable called payload and print 
the payload

### Why We Need Schema

its a pain to get all the values from the body 
the client can send whatever data they want 
they data isnt getting validated 
weultimately want to force the client to send dat in a schema
that we expect 
to do this we will use a library called pydentic 
it is installed since it is one of the dependency of the 
fast api 
you can find the documentation here 
```url
https://docs.pydantic.dev/latest/

```
to do this you will need to do the following in your code
```py
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str


@app.post('/createposts')
def create_post(post:Post):
    print(post)
    return {"messange":"you created a post"}

```
if a field is optinal you can do the following 
```py
class Post(BaseModel):
    title:str
    contnent:str 
    published:bool = True

```
in this case if the user dont provide a published field we will give a default of True

if you want a field to be optional by default ie no default value you can do the following 

```py
from typing import Optional
class Post(BaseModel):
    title:str
    contnent:str 
    published:bool = True
    rating:Optional[int] = None


```
pydantic create a model and to convert it to a python 
dictorary you will use the following code
```py
new_post.model_dump()

```
the new_post model in this case will be converted to a python 
dictorary 

the old way was to use dict() method but this is no longer supported 
