from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # Динамические данные для передачи в шаблон
    name = "Авдоничев Антон"
    profession = "Junior Python Web Developer"
    about = "Я создаю быстрые и современные сайты на FastAPI и Flask."
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "name": name,
            "profession": profession,
            "about": about
        }
    )