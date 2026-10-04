from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)

products = [
    {"id": 1, "name": "Laptop", "quantity": 10, "price": 50000},
    {"id": 2, "name": "Mouse", "quantity": 25, "price": 800},
    {"id": 3, "name": "Keyboard", "quantity": 15, "price": 1500}
]


@app.route("/")
def home():
    return "Product Inventory API is running!"


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/items")
def get_items():
    return jsonify(products)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)