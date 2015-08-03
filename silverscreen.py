#!/usr/bin/env python

from flask import make_response, Flask, request, render_template

app = Flask (__name__)


# ----- APPLICATION LOGIC -----

# TODO pass py dict of {title},{yt_url},{poster_img} passed as var to jinja

# ----- URL ROUTING -----

@app.route('/')
@app.route('/movies')
def curtains_up():
    movies = [
        {
         'title':"Fight Club",
         'yt_id': 'J8FRBYOFu2w',
         'poster_img':'http://i.jeded.com/i/fight-club.25541.jpg'
        }
        ,
        {
         'title':"Zero Theorem",
         'yt_id': 'rae7_O_6EtU',
         'poster_img':'https://resizing.flixster.com/G1Ty5AeAvPre2J8CYeLPeXrh9X4=/800x1188/dkpu1ddg7pbsk.cloudfront.net/movie/11/17/99/11179941_ori.jpg'
        }
    ]
    return render_template("movies.html", movies=movies)
    
if __name__ == '__main__':
    app.debug = "True"
    app.run(host='0.0.0.0', port=8080)
