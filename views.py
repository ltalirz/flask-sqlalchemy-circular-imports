from database import db, User
from flask.blueprints import Blueprint


people = Blueprint('people', __name__,
                 template_folder='templates',
                 static_folder='static')


@people.route('/')
def test():
  user = User.query.filter_by(username="Tom").first()
  return "Test: Username %s " % user.username
