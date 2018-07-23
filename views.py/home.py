from main import app


@app.route('/')
def hello():
    
    return 'hello from appengine'
