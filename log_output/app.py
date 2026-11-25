import os
import threading
import time
import uuid
from datetime import datetime, timezone

from flask import Flask

# Created once at startup and kept in memory
random_string = str(uuid.uuid4())
INTERVAL = 5
PORT = int(os.environ.get("PORT", 3000))


def now_iso():
    """Current time in UTC, e.g. 2026-11-25T12:45:00.123Z"""
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def log_loop():
    """Your original loop: prints timestamp + random string every 5 seconds."""
    next_tick = time.monotonic()
    while True:
        print(f"{now_iso()}: {random_string}", flush=True)
        next_tick += INTERVAL
        time.sleep(max(0, next_tick - time.monotonic()))


app = Flask(__name__)


@app.route("/")
def status():
    """The endpoint: returns the current status."""
    return f"{now_iso()}: {random_string}\n"


if __name__ == "__main__":
    # Start the log loop in the background ...
    threading.Thread(target=log_loop, daemon=True).start()
    # ... and the web server in the foreground
    app.run(host="0.0.0.0", port=PORT)
