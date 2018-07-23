from main import app
from flask import render_template


@app.route('/react')
def react():
    
    return render_template('index.html')