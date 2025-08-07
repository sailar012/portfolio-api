import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/optimal_portfolio')
def portfolio():
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]
    random.seed(42)
    w = [random.random() for _ in tickers]
    total = sum(w)
    return jsonify({
        "weights": {t: round(v/total, 4) for t, v in zip(tickers, w)},
        "expected_annual_return": round(random.uniform(0.15, 0.30), 4),
        "annual_volatility":      round(random.uniform(0.12, 0.25), 4),
        "sharpe_ratio":           round(random.uniform(1.0, 1.5), 4),
        "risk_free_rate": 0.04
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
