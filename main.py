from app import create_app, db
from app.models import User, Post

app = create_app()

# When the flask shell command runs, it will invoke this function and 
# register the items returned by it in the shell session.
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}