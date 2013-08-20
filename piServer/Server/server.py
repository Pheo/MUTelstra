# UoM Telstra M2M Challenge

# CGI Python Server (hosted on Raspberry Pi) 
# Written by Jun Min Cheong (Pheo)

################################################################################

import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable() # Error Reporting

SERVERADDR	= "" # Local Host
PORT		= 8000

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
httpd = server((SERVERADDR,PORT), handler)
httpd.serve_forever()
