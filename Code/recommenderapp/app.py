from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
import json
import sys
import time

import os
import pandas as pd
import datetime


sys.path.append("../../")
from Code.prediction_scripts.item_based import getSentimentScores, recommendForNewUser
from search import Search
from comments import Comments

app = Flask(__name__)
app.secret_key = "secret key"

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def landing_page():
    return render_template("loading.html")


@app.route("/home")
def redirected():
    return render_template("landing_page.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = json.loads(request.data)  # contains movies
    data1 = data["movie_list"]
    data1 = [s[:-1] for s in data1]
    training_data = []
    for movie in data1:
        movie_with_rating = {"title": movie, "rating": 5.0}
        training_data.append(movie_with_rating)
    recommendations = recommendForNewUser(training_data)
    recommendations = recommendations[:5]
    resp = {"recommendations": recommendations}
    print(recommendations)  # Add this line for debugging
    return resp


@app.route("/search", methods=["POST"])
def search():
    term = request.form["q"]
    print("term: ", term)

    search = Search()
    filtered_dict = search.resultsTop10(term)

    resp = jsonify(filtered_dict)
    resp.status_code = 200
    return resp


@app.route("/feedback", methods=["POST"])
def feedback():
    data = json.loads(request.data)
    
    comments = Comments()
    comments.setComments(data)

    app_dir = os.path.dirname(os.path.abspath(__file__))
    code_dir = os.path.dirname(app_dir)
    project_dir = os.path.dirname(code_dir)
    movies = pd.read_csv(project_dir + "/data/movies.csv")
    # with open(project_dir + "/data/ratings.csv", "a") as f:
    #     for key,value in data.items():
    #         print(key,"====")
    #         if type(data[key]) is list:
    #             # Find the movieId corresponding to the movie title
    #             movieId = movies.loc[movies["title"] == key, "movieId"]
    #             rating = int(data[key][0])
    #             userId = ""
    #             timestamp = int(time.time())
    #             if rating != 0:
    #                 f.write("{},{},{},{}\n".format(userId, movieId, rating, timestamp))
    
    print(data)

    # Putting data into comments.csv
    all_rows = []
    for key, value in data.items():
        if len(value[1]) > 0:  # Save only those fields that are populated
            all_rows.append(
                ["user1", "email_id<1>", key, value[1], getSentimentScores(value[1]), datetime.datetime.now()]
            )

    with open("comments.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        for row in all_rows:
            writer.writerow(row)

    return data

@app.route("/comments/<movie>")
def comments(movie):
    comments = Comments()
    movie_entries = comments.getComments(movie)
    return render_template("view_comments.html", movie_entries=movie_entries)


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
