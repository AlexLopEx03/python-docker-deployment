from wsgiref.simple_server import make_server

def app(environ, start_response):
    response_body = "¡Hola mundo!"
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)
    return [response_body.encode('utf-8')]

if __name__ == '__main__':
    with make_server('', 8080, app) as httpd:
        print("Servidor escuchando en http://localhost:8080")
        httpd.serve_forever()
