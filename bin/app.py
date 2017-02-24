#!/usr/bin/python

import web

urls = (
    '/', 'index',
    '/(.*)', 'home'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class index:
    def GET(self):
        greeting = 'Hello World'
        return render.index(greeting = greeting)

class home:
    def GET(self, name):
        return render.home(name)

if __name__ == '__main__':
    app.run()
