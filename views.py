from database import db
from flask.blueprints import Blueprint


people = Blueprint('people', __name__,
                 template_folder='templates',
                 static_folder='static')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)


@people.route('/')
def test():
  user = User.query.filter_by(username="Tom").first()
  return "Test: Username %s " % user.username
