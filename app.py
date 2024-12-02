from fastapi import FastAPI
import uvicorn

from src.engine import summarizer, entity_extractor

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/summary/{text}")
async def summry(text: str):
    return summarizer(text=text)


@app.get("/ner/{text}")
async def ner(text: str):
    return entity_extractor(text=text)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
