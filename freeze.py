from flask_frozen import Freezer
from main import app

freezer = Freezer(app)

@freezer.register_generator
def url_generator():
    yield 'home', {}
    yield 'about', {}
    yield 'contact', {}
    yield 'posts', {}

if __name__ == '__main__':
    freezer.freeze()
