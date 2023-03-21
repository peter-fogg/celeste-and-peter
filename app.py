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
