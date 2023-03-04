from fastapi import FastAPI
from book_app.router import router as book_router
from user_app.router import router as user_router

app = FastAPI()
app.include_router(user_router, tags=["user"])
app.include_router(book_router, tags=["book"])