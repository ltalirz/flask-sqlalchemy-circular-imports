from database import db
from flask import Flask
from views import User, people

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
    register_extensions(app)
    register_blueprints(app)
    return app 

def register_extensions(app):
    db.init_app(app)    

def register_blueprints(app):
    app.register_blueprint(people, url_prefix='')

def setup_database(app):
    with app.app_context():
        db.create_all()

        user = User()
        user.username = "Tom"
        db.session.add(user)
        db.session.commit()    

if __name__ == '__main__':
    app = create_app()
    setup_database(app)
    app.run()
