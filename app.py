from fastapi import FastAPI
import uvicorn

from src.engine import summarizer, entity_extractor

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/summary")
async def summry(text):
    pass


@app.get("/ner")
async def ner(text):
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
