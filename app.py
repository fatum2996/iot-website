from flask import Flask, render_template
app = Flask(__name__)

tags = ["basics", "diy", "bestof", "doorbell", "explanation", "hardware"]

playlists = {
  "main": {
    "title": "Общие положения",
    "videos": [0],
    "pic": "1.png"
  },
  "best": {
    "title": "Лучшие проекты",
    "videos": [1, 3],
    "pic": "2.jpg"
  },
  "manuals": {
    "title": "Инструкции",
    "videos": [2],
    "pic": "3.jpg"
  }
}

videos = {
  0: {"id":"0", "title":"How It Works: Internet of Things", "videoid":"QSIPNhOiMoE", "tags":[0, 4]},
  1: {"id":"1", "title":"Top 10 IoT(Internet Of Things) Projects Of All Time | 2018", "videoid":"QL-6PdiDTeo", "tags":[1, 2]},
  2: {"id":"2", "title":"Diy Door Status Notifier", "videoid":"7s0RQDi6wdo", "tags":[1, 5]},
  3: {"id":"3", "title":"Top 5 IoT Hardware Platforms", "videoid":"vZNwkPe3gyQ", "tags":[1, 2, 5]},
}


@app.route('/')
def main():
    output = render_template("main.html", tags_pick=tags, playlists_pick=playlists)
    return output


@app.route('/about')
def about():
    output = render_template("about.html")
    return output


@app.route('/videos/<id>') #добавить обработку несуществующего видео
def video(id):
    id_int = int(id)
    tag_list = []
    for tag_id in videos[id_int]["tags"]:
        tag_list.append(tags[tag_id])
    output = render_template("video.html", video_name=videos[id_int]["title"], tags=tag_list, videoid=videos[id_int]["videoid"])
    return output


@app.errorhandler(404)
def page_not_found(error):
   return "Такой страницы нет"


@app.route('/tags/<tag>') #добавить обработку несуществующего тега
def the_tag(tag):
    if tag in tags:
        tag_number = tags.index(tag)
    videos_for_tag_pick = []
    for video_value in videos.keys():
        if tag_number in videos[video_value]["tags"]:
            video_for_tag = {}
            video_for_tag["id"] = videos[video_value]["id"]
            video_for_tag["name"] = videos[video_value]["title"]
            videos_for_tag_pick.append(video_for_tag)
            print(videos_for_tag_pick)
    output = render_template("tag.html", number_of_videos=len(videos_for_tag_pick), tag_name=tag, videos_for_tag=videos_for_tag_pick)
    return output


app.run('0.0.0.0',81)    # запустим сервер на 8000 порту!