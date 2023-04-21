# Copyright (c) 2023 MediumCraft
# MediumCraft Protective License
# If the license had not came with the Software, please see https://github.com/MediumCraft/License

import http.server
import socketserver
import os

PORT = 8090 # The port of the http server
FILE_NAME = "pack.zip" # The only file accessible by the client

print("MediumCraft Resource Pack Server")
print("Starting server...")

class RestrictedHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    
    def translate_path(self, path):
        # Override base class method to restrict access to files outside of pack.zip
        full_path = os.path.join(self.document_root, FILE_NAME)
        if not os.path.exists(full_path):
            self.send_error(404, 'File Not Found')
            return "404 File Not Found"
        elif not full_path.endswith('pack.zip'):
            self.send_error(403, 'Forbidden')
            return "403 Forbidden"
        return full_path

Handler = RestrictedHTTPRequestHandler
Handler.document_root = os.path.dirname(os.path.abspath(__file__))

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}/")
    print("CTRL+C to stop the server")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Stopping server..")
    httpd.server_close()
    print(f"Server stopped.")
