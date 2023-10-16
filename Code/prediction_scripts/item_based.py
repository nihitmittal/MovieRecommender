import pandas as pd
import warnings
import os
from sklearn.metrics.pairwise import cosine_similarity

app_dir = os.path.dirname(os.path.abspath(__file__))
code_dir = os.path.dirname(app_dir)
project_dir = os.path.dirname(code_dir)

warnings.filterwarnings("ignore")

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def getSentimentScores(sentence):
    sid_obj = SentimentIntensityAnalyzer()

    sentiment_dict = sid_obj.polarity_scores(sentence)

    if sentiment_dict["compound"] >= 0.05:
        return "Supportive"

    elif sentiment_dict["compound"] <= -0.05:
        return "Critical"

    else:
        return "Neutral"


def recommendForNewUser(user_rating, num_recommendations=10):
    ratings = pd.read_csv(project_dir + "/data/ratings.csv")
    movies = pd.read_csv(project_dir + "/data/movies.csv")

    average_ratings = ratings.groupby("movieId")["rating"].mean().reset_index()
    movies = movies.merge(average_ratings, on="movieId", how="left")
    movies.rename(columns={"rating": "average_rating"}, inplace=True)

    user_movie_titles = [movie["title"] for movie in user_rating]
    userMovieID = movies[movies["title"].isin(user_movie_titles)]
    userRatings = pd.merge(userMovieID, pd.DataFrame(user_rating))

    genre_columns = movies["genres"].str.get_dummies("|")

    moviesGenreFilled = pd.concat([movies, genre_columns], axis=1)

    moviesGenreFilled.drop(["genres"], axis=1, inplace=True)

    cosine_sim = cosine_similarity(genre_columns, genre_columns)

    similarity_df = pd.DataFrame(
        cosine_sim, index=movies["movieId"], columns=movies["movieId"]
    )

    similar_movies = {}
    for movie_id in userRatings["movieId"]:
        similar_scores = (
            similarity_df.loc[movie_id]
            .sort_values(ascending=False)[1 : num_recommendations + 1]
            .index.tolist()
        )
        similar_movies[movie_id] = similar_scores

    recommendations = []
    for similar_movie_ids in similar_movies.values():
        recommended_movies = []
        for sim_movie_id in similar_movie_ids:
            sim_movie_title = movies[movies["movieId"] == sim_movie_id]["title"].values[
                0
            ]
            recommended_movies.append(
                {"title": sim_movie_title, "rating": 5.0}
            )  # Replace 5.0 with the actual rating
        recommendations.extend(recommended_movies)

    # Sort recommendations by some criteria, e.g., rating
    recommendations.sort(key=lambda x: x["rating"], reverse=True)

    # Return a list of recommended movies (titles and ratings)
    return recommendations[:num_recommendations]
