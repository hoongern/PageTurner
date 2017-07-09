from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from pywinauto import application

PORT = 8080
EXE_PATH = r"C:\\Program Files\\SumatraPDF\\SumatraPDF.exe"
KEYSTROKE = "{RIGHT}"

def main(port):
    try:
        app = application.Application().connect(path=EXE_PATH)
        print "Connected to process"
    except application.ProcessNotFoundError:
        print "Process with path '" + EXE_PATH + "' not found, starting new process"
        app = application.Application().start(EXE_PATH)
    window = app.top_window_()

    def turn_page():
        window.TypeKeys(KEYSTROKE)
        return

    class ServerHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/turn':
                self.send_response(204)
                self.end_headers()
                turn_page()
            else:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                with open('index.html', 'r') as index:
                    self.wfile.write(index.read())

    server = HTTPServer(('', port), ServerHandler)
    print 'Serving on port', port

    server.serve_forever()

if __name__ == '__main__':
    main(PORT)
