
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os   #this reads the env

load_dotenv()



db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__)
   
    if not test_config: #if test config is  none or false we want development configuration
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_TEST_URI")
    
    
    db.init_app(app)  #initialize sqlalchemy object and give the app to work with it
    migrate.init_app(app, db)  # initialize migrate object and give app to work with it and db 
    from app.models.book import Book
    
    # from .routes import hello_world_bp
    # app.register_blueprint(hello_world_bp)
    
    from .routes import books_bp 
    app.register_blueprint(books_bp)
    
    return app

    
