# 💡 IoT Light Scheduler with MQTT, WebSocket & Arduino

This project simulates a **real-world IoT dashboard** to schedule a light using a **graphical browser interface** and **network communication**. The system allows users to schedule ON/OFF times via a frontend and sends these times through a Python WebSocket server to MQTT. A Python MQTT subscriber then relays commands to an Arduino via serial to control a relay (light).

---

## 📦 Features

- ⏰ Schedule light ON/OFF times from browser
- 🌐 MQTT message relay using `mosquitto_pub/sub`
- 🔌 Arduino serial communication to switch relay
- 🖥️ Web interface with clean UI for interaction
- 🧪 Fully simulated IoT pipeline

---

## 🔧 Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend Server:** Python (`websockets`, `subprocess`)
- **MQTT Broker:** Mosquitto (test broker or local)
- **MQTT Tools:** `mosquitto_pub`, `mosquitto_sub`
- **Microcontroller:** Arduino UNO (via USB Serial)
- **Serial Comm:** `pyserial` (Python)

---

## 🗂️ Folder Structure

```bash
iot-light-scheduler/ ├── frontend/ │ └── index.html ├── websocket_server/ │ └── server.py ├── mqtt_subscriber/ │ └── subscriber.py ├── arduino/ │ └── light_controller.ino └── README.md

```


---

## 🚀 How It Works

### 1. Frontend (HTML + JS)
- Users input **ON** and **OFF** times.
- Times are sent to the WebSocket server on button click.

### 2. WebSocket Server (Python)
- Receives schedule via WebSocket from frontend.
- Forwards ON and OFF times to MQTT using `mosquitto_pub`.

### 3. MQTT Subscriber (Python)
- Uses `mosquitto_sub` to listen to schedule messages.
- Sends `ON` or `OFF` over serial (USB) to Arduino.

### 4. Arduino
- Listens via serial.
- Triggers relay based on `'1'` (ON) or `'0'` (OFF) signals.

---

## 🛠️ Setup Instructions

### Prerequisites

- Arduino IDE with code uploaded to UNO
- Python 3.11+
- Mosquitto installed (with `mosquitto_pub` and `mosquitto_sub`)
- Python packages:
  ```bash
  pip install websockets pyserial
  ```

  1. Upload Arduino Code
Upload light_controller.ino to your Arduino using the Arduino IDE.

2. Start the WebSocket Server
```bash
cd websocket_server
python server.py
```
This will listen on ws://localhost:8765.
3. Start the MQTT Subscriber
```bash
cd mqtt_subscriber
python subscriber.py
```
Make sure the COM port is correctly set in the script.

4. Open Frontend
Open frontend/index.html in your browser. Enter ON/OFF times and hit Set Schedule.
