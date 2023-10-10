# import pandas as pd
# import warnings
# import os

# app_dir = os.path.dirname(os.path.abspath(__file__))
# code_dir = os.path.dirname(app_dir)
# project_dir = os.path.dirname(code_dir)

# warnings.filterwarnings("ignore")


# def recommendForNewUser(user_rating):
#     ratings = pd.read_csv(project_dir + "/data/ratings.csv")
#     movies = pd.read_csv(project_dir + "/data/movies.csv")
#     user = pd.DataFrame(user_rating)
#     userMovieID = movies[movies["title"].isin(user["title"])]
#     userRatings = pd.merge(userMovieID, user)

#     moviesGenreFilled = movies.copy(deep=True)
#     copyOfMovies = movies.copy(deep=True)
#     for index, row in copyOfMovies.iterrows():
#         copyOfMovies.at[index, "genres"] = row["genres"].split("|")
#     for index, row in copyOfMovies.iterrows():
#         for genre in row["genres"]:
#             moviesGenreFilled.at[index, genre] = 1
#     moviesGenreFilled = moviesGenreFilled.fillna(0)

#     userGenre = moviesGenreFilled[moviesGenreFilled.movieId.isin(userRatings.movieId)]
#     userGenre.drop(["movieId", "title", "genres"], axis=1, inplace=True)
#     userProfile = userGenre.T.dot(userRatings.rating.to_numpy())
#     moviesGenreFilled.set_index(moviesGenreFilled.movieId)
#     moviesGenreFilled.drop(["movieId", "title", "genres"], axis=1, inplace=True)

#     recommendations = (moviesGenreFilled.dot(userProfile)) / userProfile.sum()
#     joinMoviesAndRecommendations = movies.copy(deep=True)
#     joinMoviesAndRecommendations["recommended"] = recommendations
#     joinMoviesAndRecommendations.sort_values(
#         by="recommended", ascending=False, inplace=True
#     )
#     return [x for x in joinMoviesAndRecommendations["title"]][:201]

import pandas as pd
import warnings
import os
from sklearn.metrics.pairwise import cosine_similarity

app_dir = os.path.dirname(os.path.abspath(__file__))
code_dir = os.path.dirname(app_dir)
project_dir = os.path.dirname(code_dir)

warnings.filterwarnings("ignore")


def recommend_movies_by_genre(user_rating, num_recommendations=10):
    # Load data
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

    similarity_df = pd.DataFrame(cosine_sim, index=movies["movieId"], columns=movies["movieId"])

    # similar_movies = {}
    # for movie_id in userRatings["movieId"]:
    #     similar_scores = similarity_df.loc[movie_id].sort_values(ascending=False)[1:num_recommendations+1].index.tolist()
    #     similar_movies[movie_id] = similar_scores

    # recommendations = {}
    # for user_movie_id, similar_movie_ids in similar_movies.items():
    #     recommended_movies = []
    #     for sim_movie_id in similar_movie_ids:
    #         sim_movie_title = movies[movies["movieId"] == sim_movie_id]["title"].values[0]
    #         recommended_movies.append(sim_movie_title)
    #     recommendations[user_movie_id] = recommended_movies

    # return recommendations
