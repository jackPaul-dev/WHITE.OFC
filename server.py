import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", os.environ.get("RAILWAY_PORT", 8080)))

print(f"Starting server on 0.0.0.0:{PORT}", flush=True)

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.html': 'text/html',
    '.css': 'text/css',
    '.js': 'application/javascript',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.ico': 'image/x-icon',
})

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Serving at http://0.0.0.0:{PORT}", flush=True)
    httpd.serve_forever()
