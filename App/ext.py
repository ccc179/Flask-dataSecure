from flask_mail import Mail
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
sess = Session()
cache = Cache()


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app, db=db)
    mail.init_app(app)
    sess.init_app(app)
    cache.init_app(app)