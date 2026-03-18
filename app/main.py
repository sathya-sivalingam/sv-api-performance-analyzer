from fastapi import FastAPI
import time
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Performance Test API"}

@app.get("/test")
def test_api():
    delay = random.uniform(0.1, 0.5)
    time.sleep(delay)
    return {
        "status": "ok",
        "response_time_simulated": delay
    }

@app.get("/heavy")
def heavy_api():
    time.sleep(1)
    return {"status": "heavy operation"}
