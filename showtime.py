#!/usr/bin/env python

from flask import make_response, Flask, request, render_template

app = Flask (__name__)

@app.route('/')
@app.route('/movies')
def curtains_up():
    
   return render_template("movies.html")
    
# TODO py dict of {title},{yt_url},{poster_img} passed as var to jinja

if __name__ == '__main__':
    app.debug = "True"
    app.run(host='0.0.0.0', port=8080)
