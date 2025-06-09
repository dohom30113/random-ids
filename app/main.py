from fastapi import FastAPI
from .api.router import router

app = FastAPI(
    title="Random ID Generator",
    description="A simple API that generates random IDs from various public APIs",
    version="1.0.0"
)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True) 