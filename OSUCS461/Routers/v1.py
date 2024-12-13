from typing import List
from fastapi import APIRouter, HTTPException
from OSUCS461.Classes.Database import UserLogic, PostLogic
from OSUCS461.Models import UserWrite, User, Post, UserPostWrite

router= APIRouter()

# get all users
@router.get("/users")
async def get_users():
    try:
        users = UserLogic.get_all_users()
        return users
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))

# get user by uuid
@router.get("/users/{user_uuid}")
async def get_user(user_uuid: str):
    try:
        user = UserLogic.get(user_uuid)
        return user
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))


#create user
@router.post("/users")
async def create_user(user: UserWrite):
    try:
        user_uuid = UserLogic.create(user)
        user = UserLogic.get(user_uuid)
        return user
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))
    

#update user
@router.put("/users/{user_uuid}")
async def update_user(user_uuid: str, user: UserWrite):
    try:
        UserLogic.update_user(user_uuid, user)
        user = UserLogic.get(user_uuid)
        return user
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))
    
#delete user
@router.delete("/users/{user_uuid}")
async def delete_user(user_uuid: str):
    try:
        UserLogic.delete(user_uuid)
        return {"status":"success"}
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))

#get all posts by user uuid
@router.get("/users/{user_uuid}/posts")
async def get_posts(user_uuid: str):
    try:
        posts = PostLogic.get_all(user_uuid)
        return posts
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))
    


#create post
@router.post("/users/{user_uuid}/posts")
async def create_post(user_uuid: str, post: UserPostWrite):
    try:
        post_uuid = PostLogic.create(user_uuid, post)
        post = PostLogic.get(user_uuid,post_uuid)
        return post
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))
    
# get post by uuid
@router.get("/users/{user_uuid}/posts/{post_uuid}")
async def get_post(user_uuid: str, post_uuid: str):
    try:
        post = PostLogic.get(user_uuid, post_uuid)
        return post
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))
    
# get all posts
@router.get("/users/{user_uuid}/posts")
async def get_all_posts(user_uuid: str):
    try:
        posts = PostLogic.get_all(user_uuid)
        return posts
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))