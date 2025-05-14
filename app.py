from bottle import Bottle, static_file, template

app = Bottle()

@app.route('/static/<filepath:path>') 
def server_static(filepath):
    return static_file(filepath, root='./static')

@app.route('/')
def index():
    return template('index')

@app.route('/projects')
def projects():
    return template('projects')

@app.route('/cg')
def cg():
    return template('cg')

@app.route('/ht')
def ht():
    return template('ht')

@app.route('/about')
def about():
    return template('about')

if __name__ == "__main__":
    app.run(host = 'localhost', port = 8000, debug = True, reloader=True) 
