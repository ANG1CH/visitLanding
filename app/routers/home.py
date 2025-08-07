from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
import httpx

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

# --- Настройки Telegram ---
TELEGRAM_BOT_TOKEN = "8437082656:AAEOsFsz9G1d7TLDe5qwF-9Sa1d7iPtGIEY"
TELEGRAM_CHAT_ID = "903259421"

async def send_telegram_message(text: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    async with httpx.AsyncClient() as client:
        await client.post(url, data=payload)

@router.post("/contact")
async def contact(
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):
    text = f"Новое сообщение с сайта!\nИмя: {name}\nEmail: {email}\nСообщение: {message}"
    await send_telegram_message(text)
    return RedirectResponse(url="/", status_code=303)