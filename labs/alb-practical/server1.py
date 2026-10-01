from http.server import BaseHTTPRequestHandler, HTTPServer


class Server1Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        message = "Response from Server 1"

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()

        self.wfile.write(message.encode())


server = HTTPServer(("localhost", 8001), Server1Handler)

print("Server 1 running on http://localhost:8001")

server.serve_forever()