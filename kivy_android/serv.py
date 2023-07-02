from http.server import BaseHTTPRequestHandler


class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # print("GET request, path:", self.path)
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("html".encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(self.path.encode('utf-8'))
        else:
            self.send_error(404, "Page Not Found {}".format(self.path))
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        try:

            if self.path == "/status":
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()

            elif self.path == "/esp":

                # outParams = json.loads(body.decode('utf-8'))
                # temp = outParams.get('Temp01', 0)  # второй аргумент это дефолтное значение, если ключ не найден в словаре
                # hum = outParams.get('Hum01', 0)  # второй аргумент это дефолтное значение, если ключ не найден в словаре

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                print("/esp")

            else:
                self.send_response(400, 'Bad Request: Method does not exist')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
        except Exception as err:
            print("do_POST exception: %s" % str(err))


if __name__ == '__main__':
    from http.server import HTTPServer

    server_address = ('', 8000)
    httpd = HTTPServer(server_address, ServerHandler)
    try:

        httpd.serve_forever()

    except KeyboardInterrupt:
        pass
    httpd.server_close()