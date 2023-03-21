import flask as f

app = f.Flask(__name__)

@app.route('/')
def index():
    return f.render_template('index.html')

@app.route('/details')
def details():
    return f.render_template('details.html')

@app.route('/durango')
def durango():
    return f.render_template('durango.html')

@app.errorhandler(404)
def not_found(error):
    return f.render_template('404.html')

@app.errorhandler(500)
def server_error(error):
    return f.render_template('500.html')
