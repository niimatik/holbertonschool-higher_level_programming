#!/usr/bin/python3
"""
Simple HTTP API Server using Python's built-in http.server module.

This module defines and runs a basic HTTP server that listens on port 8000.
It handles GET requests and provides responses for the following endpoints:

Endpoints:
- `/data`   : Returns a JSON object with sample user data.
- `/info`   : Returns a JSON object with version and description info.
- `/status` : Returns plain text 'ok' to indicate server is alive.
- `/`       : Returns a welcome message in plain text.
- any other : Returns a 404 error with 'Endpoint not found'.

Usage:
    Run this script directly with Python 3 to start the server:
        $ python3 server.py

The server runs in the foreground and logs a message indicating the port
it's listening on.

Author: [Your Name or Initials]
Date: [Optional Date]
"""

import http.server
import socketserver
import json

PORT = 8000


class FirstServer(http.server.BaseHTTPRequestHandler):
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
        """
        Handle GET requests by returning appropriate content
        based on the path.
        """
        if self.path == "/data":
            datas = {"name": "John", "age": 30, "city": "New York"}
            json_string = json.dumps(datas)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_string.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode("utf-8"))

        elif self.path == "/info":
            infos_data = {
                "version": "1.0", "description":
                "A simple API built with http.server"}
            infos_json_string = json.dumps(infos_data)
            self.send_response(200)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write(infos_json_string.encode("utf-8"))

        elif self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode("utf-8"))


if __name__ == "__main__":
    """
    Starts the TCP server on the specified PORT and
    listens indefinitely for incoming requests.
    """
    with socketserver.TCPServer(("", PORT), New_server) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()
