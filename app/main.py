from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"service": "B", "message": "Hello from Service B"}
