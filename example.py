#!/usr/bin/env python3
"""
Simple HTTP server to test Docker cache mounting
"""
import http.server
import socketserver
import os
from datetime import datetime

PORT = 8011

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html_content = f"""
            <html>
                <body>
                    <h1>Cache Test Server #2</h1>
                    <p>Server started at: {datetime.now()}</p>
                    <p>Testing Docker cache mount functionality</p>
                    <p>If cache works, pip packages should install faster on rebuilds</p>
                </body>
            </html>
            """
            self.wfile.write(html_content.encode())
        else:
            super().do_GET()

def main():
    print(f"Starting server on port {PORT}")
    print(f"Access at: http://localhost:{PORT}")
    
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"Server running at http://0.0.0.0:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            httpd.shutdown()

if __name__ == "__main__":
    main()
