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

BUS_NUM = 45

@app.route('/')
def index():
    return f.render_template('index.html')

@app.route('/details')
def details():
    return f.render_template('details.html')

@app.route('/durango')
def durango():
    return f.render_template('durango.html')

# @app.route('/rsvp', methods=['GET'])
# def rsvp():
#     return f.render_template('rsvp.html')

# @app.route('/rsvp_for', methods=['GET'])
# def rsvp_for():
#     name = f.request.args.get('name')
#     if name is None:
#         return f.redirect('/rsvp')
#     guest = db.session.query(Guest).filter(
#         func.similarity(Guest.name, name)
#         > app.config['SIMILARITY_THRESHOLD']
#     ).order_by(
#         # There is likely a more performant way to do this, but
#         # the DB is so small (< 150 names) it really won't matter
#         func.similarity(Guest.name, name).desc()
#     ).first()
#     bus_num = BUS_NUM - db.session.query(RSVP).filter_by(bus=True).count()
#     return f.render_template(
#         'rsvp_form.html',
#         guest=guest,
#         bus_num=bus_num
#     )

# @app.route('/rsvp_for', methods=['POST'])
# def rsvp_for_post():
#     form = f.request.form
#     if 'guest-id' in form: # Actually a person we want there
#         guest = db.session.execute(
#             db.select(Guest).filter_by(id=form.get('guest-id'))
#         ).scalar_one()
#         rsvp = RSVP(
#             guest_id=guest.id,
#             coming=form.get('coming') == 'coming',
#             bus=form.get('bus') == 'on',
#             diet=form.get('diet'),
#             plus_one=form.get('plus-one', default=False)
#         )
#     else: # Not invited or they typed their name horrendously wrong
#         guest = Guest(name=form.get('name'))
#         db.session.add(guest)
#         db.session.commit()
#         rsvp = RSVP(
#             guest_id=guest.id,
#             coming=form.get('coming') == 'coming',
#             bus=form.get('bus') == 'on',
#             diet=form.get('diet'),
#             plus_one=False
#         )
#     db.session.add(rsvp)
#     db.session.commit()
#     # TODO: add error handling in case of missing data/wrong name/etc.
#     if form.get('coming') == 'not-coming':
#         return f.render_template('not_coming.html')
#     return f.render_template('thanks.html', info=dict(form), guest=guest)

@app.route('/gifts')
def gifts():
    return f.render_template('gifts.html')

@app.errorhandler(404)
def not_found(error):
    return f.render_template('404.html')

@app.errorhandler(500)
def server_error(error):
    return f.render_template('500.html')
