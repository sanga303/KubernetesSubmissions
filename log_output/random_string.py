import time
import uuid
from datetime import datetime, timezone

random_string = str(uuid.uuid4())
INTERVAL = 5

next_tick = time.monotonic()
while True:
    ts = datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
    print(f"{ts}: {random_string}", flush=True)
    next_tick += INTERVAL
    time.sleep(max(0, next_tick - time.monotonic()))