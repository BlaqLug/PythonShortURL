from fastapi import FastAPI
from backend.routes import decode, encode


app = FastAPI()

app.include_router(encode.router)
app.include_router(decode.router)

@app.get("/")
def index():
    return {"Message": "URL Shortner"}

