# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify

app = Flask(__name__)

NEWS_API_KEY = None

if NEWS_API_KEY is None:
    # URL de test :
    NEWS_API_URL = "https://s3-eu-west-1.amazonaws.com/course.oc-static.com/courses/4525361/top-headlines.json" # exemple de JSON
else:
    # URL avec clé :
    NEWS_API_URL = "https://newsapi.org/v2/top-headlines?sortBy=publishedAt&pageSize=100&language=fr&apiKey=" + NEWS_API_KEY


@app.route("/")
def hello():
    return render_template('home.html')

@app.route('/predict/')
def predict():
    return render_template('predict.html')

if __name__ == "__main__":
    app.run(debug=True)