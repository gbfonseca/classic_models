from classic_models.ext.database import db
from classic_models.models import ProductLines


def init_app(app):
    @app.cli.command()
    def createdb():
        """Create Database"""
        db.create_all()
