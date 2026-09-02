from http.server import BaseHTTPRequestHandler, HTTPServer
import requests


targets = [
    "http://127.0.0.1:8001",
    "http://127.0.0.1:8002"
]

current_target = 0
class LoadBalancerHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        global current_target

        # Select a target
        target = targets[current_target]

        # Move to the next target
        current_target = (
            current_target + 1
        ) % len(targets)

        try:
            # Forward request to backend server
            response = requests.get(
                target,
                timeout=2
            )

            # Send backend response to browser
            self.send_response(response.status_code)

            self.send_header(
                "Content-Type",
                "text/plain"
            )

            self.end_headers()

            self.wfile.write(response.content)

            print(
                f"Forwarded request to {target}"
            )

        except requests.RequestException:

            self.send_response(503)

            self.end_headers()

            self.wfile.write(
                b"No healthy servers available"
            )


# Listener
server = HTTPServer(
    ("127.0.0.1", 9000),
    LoadBalancerHandler
)

print(
    "Load Balancer running on "
    "http://localhost:9000"
)

server.serve_forever()