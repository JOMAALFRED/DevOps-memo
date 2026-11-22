import json
import os
from html import escape
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

APP_NAME = "DevOps Memo Demo"
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_COLOR = os.getenv("APP_COLOR", "blue").lower()
PORT = int(os.getenv("PORT", "8080"))

PALETTE = {
    "blue": "#174C91",
    "green": "#16845B",
}

COLOR_CODE = PALETTE.get(APP_COLOR, PALETTE["blue"])


class DemoHandler(BaseHTTPRequestHandler):

    def respond(self, status, content_type, body):
        data = body.encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path = urlparse(self.path).path

        if path == "/health":
            response = {
                "status": "ok",
                "service": "devops-memo-demo"
            }
            self.respond(
                200,
                "application/json",
                json.dumps(response)
            )
            return

        if path == "/version":
            response = {
                "application": "devops-memo-demo",
                "version": APP_VERSION,
                "color": APP_COLOR
            }
            self.respond(
                200,
                "application/json",
                json.dumps(response)
            )
            return

        if path == "/":
            version = escape(APP_VERSION)
            color = escape(APP_COLOR)
            name = escape(APP_NAME)

            page = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{name}</title>
    <style>
        body {{
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f1f5f9;
            color: #1e293b;
        }}
        main {{
            max-width: 650px;
            margin: 100px auto;
            padding: 35px;
            background: white;
            border-radius: 16px;
            text-align: center;
            box-shadow: 0 8px 30px #00000012;
        }}
        .version {{
            display: inline-block;
            padding: 12px 28px;
            color: white;
            background: {COLOR_CODE};
            border-radius: 10px;
            font-size: 32px;
            font-weight: bold;
        }}
        .status {{
            color: #16845B;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <main>
        <h1>{name}</h1>
        <p>Application de démonstration Kubernetes</p>
        <div class="version">{color.upper()}</div>
        <h2>Version {version}</h2>
        <p class="status">Application opérationnelle</p>
        <p>Déployée avec Kubernetes et Argo Rollouts</p>
    </main>
</body>
</html>"""

            self.respond(200, "text/html; charset=utf-8", page)
            return

        self.respond(
            404,
            "application/json",
            json.dumps({"error": "Not Found"})
        )

    def log_message(self, format, *args):
        print(f"[HTTP] {format % args}", flush=True)


if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", PORT), DemoHandler)

    print(
        f"{APP_NAME} started: "
        f"version={APP_VERSION}, color={APP_COLOR}, port={PORT}",
        flush=True
    )

    server.serve_forever()
