from typing import Optional
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app =FastAPI()

@app.get('/blog')
def index(limit=10, published:bool =True, sort: Optional[str]=None):
    if published:
        return {'data':f'{limit} published blogs from list'}
    else:
        return {'data':f'{limit} unpublished blogs from list'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'comment':id}


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data':f"Blog is created with title {blog.title}"}
