from fastapi import WebSocket

async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    while True:

        text = await websocket.receive_text()

        await websocket.send_text(f"Agent received: {text}")