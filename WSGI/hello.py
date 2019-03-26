def application(environ, start_reponse):
    start_reponse('200 OK', [('Content-Type', 'text/html')])
    s = '<h1>Hello,%s!</h1>' % environ['PATH_INFO'][1:]
    return [s.encode('utf-8')]
