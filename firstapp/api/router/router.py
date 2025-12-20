from fastapi import APIRouter
from fastapi.requests import Request
from ...schemas.schemas import UserModel, LoginModel
from ...database.model import User
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from mongoengine.connection import get_connection
import os
v1 = APIRouter()

templates = Jinja2Templates(directory= f"{os.getcwd()}/firstapp/templates")


@v1.get('/home')
def home(request: Request):
    return templates.TemplateResponse("register.html",{"request": request})

@v1.post('/users/register')
def register(user: UserModel):
    try:

        user_obj= User(name=user.name, email=user.email, address=user.address, dob=user.dob, password=user.password)
        user_obj.set_password(user.password)
        user_obj.save()
        return JSONResponse ({"success": True, "data": {"id": str(user_obj.id)}})
    except Exception as e:
        return JSONResponse({"success": False, "error": str(e)})

@v1.post("/users/login")
def login(cred: LoginModel):
    try:
        usr = User.objects(email=cred.username).first()
        if usr:
            if usr.check_password(cred.password):
                return {"success": True}
            else:
                return {"success": False, "message": "Invalid credentials"}
        else:
            return {"success": False, "message": "Invalid credentials"}
    except Exception as e:
        return {"success": False, "message": f"Error occured {e}"}