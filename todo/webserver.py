# File: simplehttpserver-example-1.py

import http.server
import socketserver

# minimal web server.  serves files relative to the
# current directory.

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()

## $ python simplehttpserver-example-1.py
## serving at port 8000
## localhost - - [11/Oct/1999 15:07:44] code 403, message Directory listing
## not supported
## localhost - - [11/Oct/1999 15:07:44] "GET / HTTP/1.1" 403 -
## localhost - - [11/Oct/1999 15:07:56] "GET /samples/sample.htm HTTP/1.1" 200 -