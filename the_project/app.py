import os
import socket
from datetime import datetime, timezone
from flask import Flask

app = Flask(__name__)

PORT = int(os.environ.get("PORT", 3000))
NODE_NAME = os.environ.get("NODE_NAME", "unknown")
STARTED = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


@app.route("/")
def index():
    pod_name = socket.gethostname()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    return f"""<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Todo app</title>
    <style>
      body {{
        font-family: -apple-system, sans-serif;
        background: #f0f4f8;
        display: flex;
        justify-content: center;
        padding-top: 60px;
      }}
      .card {{
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
        padding: 24px 32px;
        min-width: 360px;
      }}
      h1 {{ margin-top: 0; }}
      table {{ border-collapse: collapse; width: 100%; }}
      td {{ padding: 8px 0; border-bottom: 1px solid #eee; }}
      td:first-child {{ color: #666; width: 90px; }}
      code {{ background: #eef2f7; padding: 2px 6px; border-radius: 4px; }}
    </style>
  </head>
  <body>
    <div class="card">
      <h1>Todo app</h1>
      <p>Running in Kubernetes 🚀</p>
      <table>
        <tr><td>Pod</td><td><code>{pod_name}</code></td></tr>
        <tr><td>Node</td><td><code>{NODE_NAME}</code></td></tr>
        <tr><td>Port</td><td><code>{PORT}</code></td></tr>
        <tr><td>Started</td><td>{STARTED}</td></tr>
        <tr><td>Now</td><td>{now}</td></tr>
      </table>
    </div>
  </body>
</html>
"""


if __name__ == "__main__":
    print(f"Server started in port {PORT}", flush=True)
    app.run(host="0.0.0.0", port=PORT)
