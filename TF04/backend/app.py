from flask import Flask, jsonify
import socket
import time
import random
from config import INSTANCE_ID, INSTANCE_NAME, PORT

app = Flask(__name__)
start_time = time.time()
request_count = 0


@app.route("/api/info")
def info():
    global request_count
    request_count += 1
    return jsonify({
        "instance_id": INSTANCE_ID,
        "instance_name": INSTANCE_NAME,
        "hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "uptime": round(time.time() - start_time, 2),
        "requests_served": request_count
    })


@app.route("/api/products")
def products():
    produtos = [
        {"id": 1, "name": "Notebook Gamer", "price": 4599.90, "stock": 15},
        {"id": 2, "name": "Mouse Wireless", "price": 89.90, "stock": 200},
        {"id": 3, "name": "Teclado Mecânico", "price": 349.90, "stock": 80},
        {"id": 4, "name": "Monitor 27\"", "price": 1899.90, "stock": 30},
        {"id": 5, "name": "Headset RGB", "price": 259.90, "stock": 120},
        {"id": 6, "name": "Webcam HD", "price": 199.90, "stock": 60},
    ]
    return jsonify({"products": produtos, "served_by": INSTANCE_ID})


@app.route("/api/cart", methods=["GET"])
def cart():
    return jsonify({
        "items": [],
        "total": 0,
        "served_by": INSTANCE_ID
    })


@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "instance_id": INSTANCE_ID,
        "uptime": round(time.time() - start_time, 2)
    })


@app.route("/api/status")
def status():
    return jsonify({
        "instance_id": INSTANCE_ID,
        "instance_name": INSTANCE_NAME,
        "hostname": socket.gethostname(),
        "uptime": round(time.time() - start_time, 2),
        "requests_served": request_count,
        "status": "running"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
