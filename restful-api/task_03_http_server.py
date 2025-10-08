#!/usr/bin/python3
"""Module that add a class who deal with the requests of web site, and a script
that start a local http server"""
import http.server
import socketserver
import json

PORT = 8000


class FirstServer(http.server.BaseHTTPRequestHandler):
"""Class that deal with the requests of the users"""
    def do_GET(self):
        """All the methods to deal with some endpoints"""
        if self.path == "/data":
            datas = {"name": "John", "age": 30, "city": "New York"}
            json_string = json.dumps(datas)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_string.encode("utf-8"))

        elif self.path == "/info":
            infos = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            json_string = json.dumps(infos)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_string.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("ok".encode("utf-8"))

        elif self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode("utf-8"))


if __name__ == "__main__":
    """
    Starts the TCP server on the specified PORT and
    listens indefinitely for incoming requests.
    """
    with socketserver.TCPServer(("", PORT), FirstServer) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()
