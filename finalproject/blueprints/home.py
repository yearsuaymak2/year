from flask import Blueprint, render_template, request
import json
import requests

video = Blueprint('video', __name__)

url = "127.0.0.1:5000/lyrics"

headers = {
    'username': "admin",
    'password': "admin"
    }


@home.route('/')
def index():
    response = requests.request("GET", url, headers=headers).json()
    lyrics  = []
    for i in range(0, 4):
        lyrics.append(
            {"title":response['results'][i]['title'],
            "artist":response['results'][i]['artist'],
            "web_url":response['results'][i]['web_url']
            })
    return render_template("home.html", lyrics=lyrics, margins=["150px", "100px", "50px", "30px"])



@home.route('/video/<title>')
def video_page(title):
    response = None
    video = None
    try:
        response = requests.request("GET", url, headers=headers, params={"query":title, "number":"1"}).json()
        video = response['Hip-Hop/Rap'][0]['title']
        video = response['artist'][0]['title']
        video = response['album'][0]['title']
        video = response['year'][0]['title']
        video = response['country'][0]['title']
        video = response['genre'][0]['title']
        video = response['web_url'][0]['title']
        video = response['img_url'][0]['title']
        video = response['yt_url'][0]['title']
    except:
        return render_template("main.html", video=-1)
    return render_template("main.html", video=video)