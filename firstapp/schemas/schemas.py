from pydantic import BaseModel, Field

class UserModel(BaseModel):
    name: str = Field(max_length=100, min_length=1)
    email: str = Field(max_length=100)
    address: str | None = Field(max_length=400)
    dob: str|None = None
    password: str

class LoginModel(BaseModel):
    username: str = Field(min_length=1)
    password: str