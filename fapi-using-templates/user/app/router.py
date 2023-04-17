from fastapi import APIRouter,Request,Form,status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,RedirectResponse
from .models import User

router=APIRouter()

templates=Jinja2Templates(directory="app/templates")

@router.get("/",response_class=HTMLResponse)
async def read_item(request:Request):
    return templates.TemplateResponse("signup.html",{"request":request})

@router.post("/ragistration/",response_class=HTMLResponse)
async def read_item(request:Request,Name:str=Form(...),
                    Email:str=Form(...),
                    Phone:str=Form(...),
                    Password:str=Form(...)):
    
    if await User.filter(email=Email).exists():
        return RedirectResponse("/",status_code=status.HTTP_302_FOUND)
    
    elif await User.filter(phone=Phone).exists():
        return RedirectResponse("/",status_code=status.HTTP_302_FOUND)
    
    else:
        user_obj=await User.create(email=Email,name=Name,phone=Phone,password=Password)
        return RedirectResponse("/login/",status_code=status.HTTP_302_FOUND)