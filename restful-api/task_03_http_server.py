#!/usr/bin/python3
"""A simple HTTP server implementing a basic API."""
import http.server
import requests
import json

PORT = 8000


class HTTPRequest(http.server.BaseHTTPRequestHandler):
    """Handle HTTP requests for the API."""
    def do_GET(self):
        """Process GET requests and return appropriate responses."""
        if self.path == '/data':
            dataset = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(dataset).encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode('utf-8'))
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info_msg = {"version": "1.0",
                        "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info_msg).encode('utf-8'))
        elif self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        else:
            self.send_error(404, "Not found")
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_msg = "Endpoint not found"
            self.wfile.write(json.dumps(error_msg).encode('utf-8'))


server = http.server.HTTPServer(('', PORT), HTTPRequest)
server.serve_forever()
server.server_close()
