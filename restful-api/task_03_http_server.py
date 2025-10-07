#!/usr/bin/python3
import http.server
import socketserver
import json

PORT = 8000


class first_server(http.server.BaseHTTPRequestHandler):
    """
    A simple HTTP server handler that responds to specific GET requests.

    Endpoints:
    - /data: Returns JSON data with a sample user info.
    - /info: Returns JSON data with version and description info.
    - /status: Returns plain text 'ok' indicating the server is running.
    - /: Returns a welcome message as plain text.
    Other paths return a 404 error with 'Endpoint not found'.
    """

    def do_GET(self):
        """Handle GET requests by returning
        appropriate content based on the path."""
        if self.path == "/data":
            datas = {"name": "John", "age": 30, "city": "New York"}
            json_string = json.dumps(datas)
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_string.encode("utf-8"))
        elif self.path == "/info":
            infos = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            json_string = json.dumps(infos)
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_string.encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write("ok".encode("utf-8"))
        elif self.path == "/":
            self.send_response(200)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers
            self.wfile.write("Endpoint not found")


if __name__ == "__main__":
    """Starts the TCP server on the specified PORT and
    listens indefinitely for incoming requests."""
    with socketserver.TCPServer(("", PORT), first_server) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
