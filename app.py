from flask import Flask, render_template, request, jsonify
from data import PHARMACY_DATA

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search_medicine():
    payload = request.json
    medicine = payload.get("medicine", "").lower()

    # 1. Filter by medicine name
    matched = [
        p for p in PHARMACY_DATA
        if medicine in p["medicine"].lower()
    ]

    # 2. Filter only AVAILABLE stock
    available = [p for p in matched if p["available"]]

    # 3. Sort by: distance → delivery time → price
    available_sorted = sorted(
        available,
        key=lambda x: (x["distance_km"], x["delivery_minutes"], x["price"])
    )

    return jsonify({
        "total_apps_checked": len(matched),
        "available_count": len(available_sorted),
        "results": available_sorted
    })

if __name__ == "__main__":
    app.run()
