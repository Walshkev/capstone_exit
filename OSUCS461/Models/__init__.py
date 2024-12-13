from pydantic import BaseModel

class BasePydanticModel(BaseModel):
	class Config:
		from_attributes = False
		validate_assignment = True

# model one: user
# create user 

class UserWrite(BaseModel):
    name: str


class User(UserWrite):
    uuid: str = '0'
    time_created: int



class Post(BaseModel):
    uuid: str = '0'
    time_created: int


class UserPostWrite(BaseModel):
      text: str

class UserPost(UserPostWrite):
    uuid: str = '0'
    post_9char:str
    user_uuid : str
    time_created: int