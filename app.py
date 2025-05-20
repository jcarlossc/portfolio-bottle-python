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

@app.route('/project1')
def project1():
    return template('project1')

@app.route('/project2')
def project2():
    return template('project2')

@app.route('/project3')
def project3():
    return template('project3')

@app.route('/project4')
def project4():
    return template('project4')

@app.route('/project5')
def project5():
    return template('project5')

@app.route('/project6')
def project6():
    return template('project6')

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
