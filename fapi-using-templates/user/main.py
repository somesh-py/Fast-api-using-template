from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app import router as UserRoute

app=FastAPI()
app.include_router(UserRoute.router)

register_tortoise(
    app,
    db_url="postgres://postgres:root@127.0.0.1/practice",
    modules={'models':['app.models']},
    generate_schemas=True,
    add_exception_handlers=True
)