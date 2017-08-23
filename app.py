from database import db
from flask import Flask
import os.path
from views import User
from views import people


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
    db.init_app(app)    
    app.register_blueprint(people, url_prefix='')
    return app 


def setup_database(app):
    with app.app_context():
        db.create_all()
    user = User()
    user.username = "Tom"
    db.session.add(user)
    db.session.commit()    


if __name__ == '__main__':
    app = create_app()
    # Because this is just a demonstration we set up the database like this.
    if not os.path.isfile('/tmp/test.db'):
      setup_database(app)
    app.run()
