from bottle import Bottle, static_file, template

app = Bottle()

@app.route('/static/<filepath:path>') 
def server_static(filepath):
    return static_file(filepath, root='./static')

@app.route('/')
def index():
    return template('index')

if __name__ == "__main__":
    app.run(host = 'localhost', port = 8000, debug = True, reloader=True) 
