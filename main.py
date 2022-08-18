from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np


app = FastAPI()
my_posts = [
    {"title": "Post 1", "content": "Content of post 1", "id": 1},
    {"title": "Post 2", "content": "Content of post 2", "id": 2},
    {"title": "Post 3", "content": "Content of post 3", "id": 3},
]


# USING FUNCTIONS
def find_max_id():
    posts_id = []
    for post in my_posts:
        posts_id.append(post['id'])
    return int(np.max(posts_id))


def find_post_by_id(id):
    for post in my_posts:
        if int(post['id']) == int(id):
            return post


def create_post_by_content(content):
    for post in my_posts:
        if (int(post['id']) == int(id)):
            new_post = content.dict()
            new_post['id'] = find_max_id() + 1
            my_posts.append(new_post)
            return new_post


def delete_post_by_id(id):
    for post in my_posts:
        if (int(post['id']) == int(id)):
            my_posts.remove(post)
            return my_posts


def change_post_by_id(id, content):
    for post in my_posts:
        if (int(post['id']) == int(id)):
            my_posts.remove(post)
            new_post = content.dict()
            new_post['id'] = int(id)
            return new_post


# SCHEMA
class Post(BaseModel):
    title: str
    content: str


# POST REQUEST
@app.post('/posts')
async def create_post(new_post: Post):
    result = create_post_by_content(new_post)
    return {"data": result}


# GET REQUEST
@app.get('/posts')
async def get_posts():
    result = my_posts
    return {"data": result}


@app.get('/posts/{id}')
def get_post(id):
    result = find_post_by_id(id)
    return {"data": result}


# PUT/PATCH REQUEST
@app.put('/posts/{id}')
async def change_whole_post(id, edited_post: Post):
    result = change_post_by_id(id, edited_post)
    return {"data": result}


# DELETE REQUEST
@app.delete('/posts/{id}')
async def delete_post(id):
    result = delete_post_by_id(id)
    return {"data": result}
