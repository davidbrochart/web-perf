from anyio.lowlevel import checkpoint
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    await checkpoint()
    return {"Hello": "World"}
