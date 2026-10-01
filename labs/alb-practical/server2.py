from http.server import BaseHTTPRequestHandler, HTTPServer


class Server2Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        message = "Response from Server 2"

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()

        self.wfile.write(message.encode())


server = HTTPServer(("localhost", 8002), Server2Handler)

print("Server 2 running on http://localhost:8002")

server.serve_forever()