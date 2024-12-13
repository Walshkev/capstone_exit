from OSUCS461.Config import MySQL as DatabaseConfig
from OSUCS461.ThirdParty.MySQL import MySQL
from OSUCS461.Models import User, Post, UserPost, UserWrite, UserPostWrite


from OSUCS461.Utilities import createHash,nowSeconds
from typing import List
import time 




DB = MySQL(**DatabaseConfig)


class UserLogic:
    table = "user"

    #make a user in the database
    @staticmethod
    def create(user:UserWrite ) -> str:
        uuid = createHash(UserLogic.table)
        result= DB.Add(UserLogic.table, data={
            "uuid":uuid, 
            "name":user.name,
            "time_created":nowSeconds()})

        return result["uuid"]
    
    # get all users from the database
    @staticmethod
    def get_all_users() -> List[User]:
        result = DB.GetAll(UserLogic.table)
        return list(map(lambda r: User(**r), result))


    #get a user with a specific uuid from the database
    @staticmethod
    def get(uuid: str) -> User:
        result = DB.GetBy(UserLogic.table, field_params={"uuid":uuid})
        return User(**result)
    
    #delete a user with a specific uuid from the database
    @staticmethod
    def delete(uuid: str)-> bool:
        result = DB.DeleteWhere(UserLogic.table, field_params={"uuid":uuid})
        return result["result"]
    
    #update a user with a specific uuid from the database
    @staticmethod
    def update_user(uuid: str, user: UserWrite)-> bool:
        return  DB.Update(UserLogic.table,data={"name":user.name}, field_params={"uuid":uuid})
        


class PostLogic:
    table = "user_post"

    # create a post in the database
    @staticmethod
    def create(user_uuid:str, post: UserPostWrite) -> str:
        uuid = createHash(PostLogic.table)
        result= DB.Add(PostLogic.table, data={
            "uuid":uuid, 
            "user_uuid":user_uuid,
            "post_9char":post.text[:9],
            "text":post.text, 
            "time_created":nowSeconds()})

        return result["uuid"]
    
    # get all posts from the database
    @staticmethod
    def get_all(user_uuid:str):
        result = DB.GetAllWhere(PostLogic.table, field_params={"user_uuid":user_uuid})
        return list(map(lambda r: Post(**r), result))


    # get a post with a specific uuid from the database
    @staticmethod
    def get(user_uuid:str ,uuid: str) -> Post:
        result = DB.GetBy(PostLogic.table, field_params={"uuid":uuid, "user_uuid": user_uuid})
        return Post(**result)

