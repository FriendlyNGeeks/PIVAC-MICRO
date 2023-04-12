try:
  import usocket as socket
except:
  import socket
  
from machine import Pin
import network


with open('index.html', 'r') as f:
    html_string = f.read()
# START WEB SERVER
#####################################################################
# Python 3 server example
#from http.server import BaseHTTPRequestHandler, HTTPServer
#import json

#server_address = ('0.0.0.0', 80)

'''class MyServer(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.wfile.write(bytes("<html><head><title>PiVAC SERVER API</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Payload has not yet been loaded or can not be found. Please try again later or contact support</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
'''
class startApi():
    def start():
        def web_page():
            html = html_string
            return html  
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 80))
        s.listen(5)
        print('API server started')
        while True:
            conn, addr = s.accept()
            print('Got a connection from %s' % str(addr))
            request = conn.recv(1024)
            request = str(request)
            print('Content = %s' % request)
            '''led_on = request.find('/?led=on')
            led_off = request.find('/?led=off')
            if led_on == 6:
                print('LED ON')
                led.value(1)
            if led_off == 6:
                print('LED OFF')
                led.value(0)'''
            response = web_page()
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response)
            conn.close()
    # if __name__ == "__main__":
        '''webServer = HTTPServer(server_address, MyServer)
        print("Server started http://%s:%s" % server_address)

        try:
            webServer.serve_forever()
            print("it started for real")
        except KeyboardInterrupt:
            pass

        webServer.server_close()
        print("Server stopped.")'''
#####################################################################
# END WEB SERVER