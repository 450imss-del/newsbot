import feedparser
from flask import Flask, jsonify
import time

app = Flask(__name__)

KEYWORDS = ["bloqueo", "balacera", "narcobloqueo", "operativo", "código rojo"]

FEEDS = [
    "https://news.google.com/rss/search?q=México+violencia",
    "https://news.google.com/rss/search?q=Jalisco+bloqueos",
    "https://news.google.com/rss/search?q=autopista+México+Puebla"
]

def get_news():
    alerts = []
    for feed in FEEDS:
        d = feedparser.parse(feed)
        for entry in d.entries[:10]:
            title = entry.title.lower()
            if any(k in title for k in KEYWORDS):
                alerts.append({
                    "title": entry.title,
                    "link": entry.link,
                    "time": time.strftime("%Y-%m-%d %H:%M:%S")
                })
    return alerts

@app.route("/")
def home():
    return "Bot funcionando"

@app.route("/news")
def news():
    return jsonify(get_news())

app.run(host="0.0.0.0", port=10000)
