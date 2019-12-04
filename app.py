from flask import Flask, render_template
app = Flask(__name__)

tags = ["basics", "diy", "bestof", "doorbell", "explanation", "hardware"]

playlists = {
  "main": {
    "title": "Общие положения",
    "videos" : [0]
  },
  "best": {
    "title": "Лучшие проекты",
    "videos" : [1, 3]
  },
  "manuals": {
        "title": "Инструкции",
        "videos": [2]
  }
}

videos = {
  0: {"id":"0", "title":"How It Works: Internet of Things", "videoid":"QSIPNhOiMoE", "tags":[0, 4]},
  1: {"id":"1", "title":"Top 10 IoT(Internet Of Things) Projects Of All Time | 2018", "videoid":"QL-6PdiDTeo", "tags":[1, 2, 3]},
  2: {"id":"2", "title":"Diy Door Status Notifier", "videoid":"7s0RQDi6wdo", "tags":[1, 5]},
  3: {"id":"3", "title":"Top 5 IoT Hardware Platforms", "videoid":"vZNwkPe3gyQ", "tags":[1, 5, 2]},
}

@app.route('/')
def main():
    return '0'

@app.route('/about')
def about():
    output = render_template("about.html")
    return output

@app.route('/videos/<id>')
def video(id):
    output = render_template("video.html")
    return output
@app.errorhandler(404)
def page_not_found(error):
   return "Такой страницы нет"

app.run('0.0.0.0',81)    # запустим сервер на 8000 порту!