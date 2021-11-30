from uvicorn import run
from fastapi import FastAPI

app = FastAPI(
    title="Okteto Gateway example",
    description="Example of using jetbrains gateway + okteto to provision entire dev environments ide included inside kubernetes",
    version="0.0.1",
    redoc_url=None,
)


@app.get("/")
def root():
    return "hello world"


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8080)
