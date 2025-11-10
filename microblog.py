import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db, cli
from app.models import User, Post
from translate import translate
translate.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}