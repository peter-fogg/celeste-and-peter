import os

import flask as f

from models import db

app = f.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return f.render_template('index.html')

@app.route('/details')
def details():
    return f.render_template('details.html')

@app.route('/durango')
def durango():
    return f.render_template('durango.html')

@app.route('/rsvp', methods=['GET'])
def rsvp():
    return f.render_template('rsvp.html')

@app.route('/rsvp', methods=['POST'])
def rsvp_post():
    form = f.request.form
    if form.get('coming') is None:
        return f.render_template('not_coming.html')
    # TODO: add error handling in case of missing data/wrong name/etc.
    return f.render_template('thanks.html', info=dict(form))

@app.errorhandler(404)
def not_found(error):
    return f.render_template('404.html')

@app.errorhandler(500)
def server_error(error):
    return f.render_template('500.html')
