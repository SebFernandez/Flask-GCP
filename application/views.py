from application import app
from flask import request, render_template

@app.route ("/")
def index ():
    args = None
    
    if request.args:
        args = request.args
    
    return render_template ("public/index.html", argument=args)