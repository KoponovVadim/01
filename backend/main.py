from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import smtplib

from email.mime.text import MIMEText

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Lead(BaseModel):
    name: str
    contact: str
    message: str = ""

@app.post("/api/lead")
async def send_lead(data: Lead):

    body = f"""
Новая заявка

Имя: {data.name}
Контакт: {data.contact}

Сообщение:
{data.message}
"""

    msg = MIMEText(body)

    msg["Subject"] = "01Вкладка — новая заявка"
    msg["From"] = "privet@01вкладка.рф"
    msg["To"] = "privet@01вкладка.рф"

    server = smtplib.SMTP_SSL(
        "mail.beget.com",
        465
    )

    server.login(
        "privet@01вкладка.рф",
        "Yuf8exju*"
    )

    server.send_message(msg)

    server.quit()

    return {
        "ok": True
    }