from fastapi import FastAPI
from agent.agent import process_request
import time

app = FastAPI()

@app.get("/")
def health():
    return {"status": "Voice AI Agent Running"}

@app.post("/chat")
def chat(user_text: str, session_id: str = "default"):

    start = time.time()

    response = process_request(user_text, session_id)

    latency = (time.time() - start) * 1000
    print(f"Latency: {latency} ms")

    return {
        "response": response,
        "latency_ms": latency
    }