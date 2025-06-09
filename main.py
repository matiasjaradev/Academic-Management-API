from fastapi import FastAPI
from routers import user, security,studients, subjects

app = FastAPI()

app.include_router(user.router)
app.include_router(security.router)
app.include_router(studients.router)
app.include_router(subjects.router)