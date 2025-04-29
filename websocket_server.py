import asyncio
import websockets
import json
import os

MQTT_TOPIC_ON = "light/schedule/on"
MQTT_TOPIC_OFF = "light/schedule/off"
MQTT_HOST = "localhost"  # or your broker IP

async def handle(websocket):
    async for message in websocket:
        print("Received from browser:", message)
        data = json.loads(message)
        on_time = data.get("on")
        off_time = data.get("off")
        if on_time:
            os.system(f"mosquitto_pub -h {MQTT_HOST} -t {MQTT_TOPIC_ON} -m {on_time}")
        if off_time:
            os.system(f"mosquitto_pub -h {MQTT_HOST} -t {MQTT_TOPIC_OFF} -m {off_time}")
        print(f"Published: ON @ {on_time}, OFF @ {off_time}")

async def main():
    async with websockets.serve(handle, "localhost", 6789):
        print("WebSocket Server listening on ws://localhost:6789")
        await asyncio.Future()  # run forever

asyncio.run(main())
