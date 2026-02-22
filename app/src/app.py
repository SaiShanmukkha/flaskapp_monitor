import logging
import random
import time

from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s level=%(levelname)s msg=%(message)s",
)

REQ = Counter("app_requests_total", "Total requests", ["route", "method", "code"])
LAT = Histogram("app_request_duration_seconds", "Request latency", ["route"])

@app.get("/")
def home():
    start = time.time()
    time.sleep(random.uniform(0.02, 0.25))

    if random.random() < 0.1:
        REQ.labels(route="/", method="GET", code="500").inc()
        logging.error("request_failed route=/ reason=simulated_error")
        return "error\n", 500

    REQ.labels(route="/", method="GET", code="200").inc()
    LAT.labels(route="/").observe(time.time() - start)
    logging.info("request_ok route=/")
    return "ok\n", 200

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)