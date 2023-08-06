from fastapi import FastAPI, BackgroundTasks
from config import MailBody
from sender import send_mail

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/send-email")
async def schedule_mail(req: MailBody, tasks: BackgroundTasks):
    data = req.dict()
    tasks.add_task(send_mail, data)
    return {"status": 200, "message": "email has been scheduled"}

