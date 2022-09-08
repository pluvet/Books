from flask import Flask
from source.controllers.book_flask import book_blueprint

app = Flask(__name__)
app.register_blueprint(book_blueprint)

@app.errorhandler(Exception)
def handle_error(error):
    """ Handle BluePrint JSON Error Response """
    response = {
        'error': error.__class__.__name__
    }
    return response, 500

#pytest no interactuar con servicios externos
