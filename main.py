import logging
from flask import Flask


app = Flask(__name__)

import views


@app.errorhandler(500)
def server_error(e):

    logging.exception('An error occurred during a request.')
    
    return 'An internal error occurred.', 500
