import os

import flask as f
from sqlalchemy import func

from models import db, RSVP, Guest

app = f.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SIMILARITY_THRESHOLD'] = os.environ['SIMILARITY_THRESHOLD']

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

@app.route('/rsvp_for', methods=['GET'])
def rsvp_for():
    name = f.request.args.get('name')
    if name is None:
        similar_names = db.session.query(Guest).all()
    else:
        similar_names = db.session.query(Guest).filter(
            func.similarity(Guest.name, name)
            > app.config['SIMILARITY_THRESHOLD']
        ).order_by(
            # There is likely a more performant way to do this, but
            # the DB is so small (< 150 names) it really won't matter
            func.similarity(Guest.name, name).desc()
        ).all()
    return f.render_template('rsvp_form.html', similar_names=similar_names)

@app.route('/rsvp_for', methods=['POST'])
def rsvp_for_post():
    form = f.request.form
    rsvp = RSVP(
        guest_id=db.session.execute(db.select(Guest).filter_by(name=form.get('name'))).scalar_one().id,
        coming=form.get('coming') == 'coming',
        guests=form.get('guests'),
        bus=form.get('bus'),
        diet=form.get('diet')
    )
    db.session.add(rsvp)
    db.session.commit()
    # TODO: add error handling in case of missing data/wrong name/etc.
    if form.get('coming') == 'not-coming':
        return f.render_template('not_coming.html')
    return f.render_template('thanks.html', info=dict(form))

@app.errorhandler(404)
def not_found(error):
    return f.render_template('404.html')

@app.errorhandler(500)
def server_error(error):
    return f.render_template('500.html')
