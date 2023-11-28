# <i>Movie Recommendation 🎥 </i>


<h2 style="text-align: center; color:#9EF8EE">A Collaborative Filtering-Based Recommendation System<h2>
  
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/nihitmittal)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)]([https://forthebadge.com](https://github.com/nihitmittal/MovieRecommender))
[![forthebadge](https://forthebadge.com/images/badges/made-with-javascript.svg)]([https://forthebadge.com](https://github.com/nihitmittal/MovieRecommender))


[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/nihitmittal/MovieRecommender/graphs/commit-activity)
[![Contributors Activity](https://img.shields.io/github/commit-activity/m/nihitmittal/MovieRecommender)](https://github.com/nihitmittal/MovieRecommender/pulse)
![GitHub contributors](https://img.shields.io/github/contributors/nihitmittal/MovieRecommender)
![Test Workflow](https://github.com/raghavnarula/MovieRecommender/actions/workflows/test.yml/badge.svg)
[![GitHub issues](https://img.shields.io/github/issues/nihitmittal/MovieRecommender.svg)](https://github.com/nihitmittal/MovieRecommender/issues)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/nihitmittal/MovieRecommender.svg)](https://github.com/nihitmittal/MovieRecommender/issues?q=is%3Aissue+is%3Aclosed)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
![Code Coverage](https://img.shields.io/badge/coverage-99.4%25-light_green)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10211139.svg)](https://doi.org/10.5281/zenodo.10211139)
[![GitHub release](https://img.shields.io/github/tag/nihitmittal/MovieRecommender.svg )](https://github.com/nihitmittal/MovieRecommender/tags)
[![black](https://img.shields.io/badge/StyleChecker-black-purple.svg)](https://pypi.org/project/black/)
![GitHub repo size](https://img.shields.io/github/repo-size/nihitmittal/MovieRecommender)
![GitHub release](https://img.shields.io/github/release/nihitmittal/MovieRecommender.svg)
[![HitCount](https://hits.dwyl.com/nihitmittal/MovieRecommender.svg?style=flat-square)](http://hits.dwyl.com/nihitmittal/MovieRecommender)
![GitHub Release Date - Published_At](https://img.shields.io/github/release-date/nihitmittal/MovieRecommender)


<h2>Brief Introduction Plan</h2>

Content Based Recommender System recommends movies similar to the movie user likes and analyses the sentiments on the reviews given by the user for that movie.

The details of the movies(title, genre, runtime, rating, poster, etc) are fetched using an API by TMDB, https://www.themoviedb.org/documentation/api, and using the IMDB id of the movie in the API, I did web scraping to get the reviews given by the user in the IMDB site using beautifulsoup4 and performed sentiment analysis on those reviews.

<h2>Documentation</h2>

The detailed documentation of our project can be found on the [Wiki Page](https://github.com/nihitmittal/MovieRecommender/wiki)
<h2>Tech stack 👨‍💻</h2>

|<img src="images/python.svg">     | <img src="images/flask.svg">      | <img src="images/html5.svg">         |<img src="images/css3.svg">       | <img src="images/javascript.svg">        | 
| -------- | ------- | -------- | ------- | -------|
| Python | Flask     | HTML | CSS     | Javascript |


<h2>Working 📱</h2>
Click on the picture to watch the movie

[![Alt text](https://github.com/nihitmittal/MovieRecommender/blob/master/asset/Movie-Recommendation.jpeg)](https://youtu.be/IsLc_Nr0rak)

<h2>Requirements and Setup ⚙️</h2>

- Python 3.9 + [Install Python On Your System](https://docs.python.org/3.9/using/index.html)
- Style check - black
  ``` bash
  pip install black
  ```
- Clone the git repository
  ``` bash
  git clone https://github.com/nihitmittal/MovieRecommender.git
  ```
- Install all required Python packages
  ``` bash
  pip install -r requirements.txt
  ```
**Now, You good to go and enjoy watching the recommended movies** 

<h2>Usage</h2>

``` bash
cd Code/recommenderapp
python3 app.py
```
![Intial](https://github.com/nihitmittal/MovieRecommender/assets/52000096/79b54bfc-4ff1-478e-838a-6f36a8205d01)

<h2>Major Parts of the Project  </h2>
<h3>Recommendation Mechanism</h3>

How does it decide which item is most similar to the item user likes? Here come the similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

![mechanism](https://github.com/nihitmittal/MovieRecommender/assets/52000096/25434790-4c08-4563-b7d0-0d2470dfa5b7)

<h3>Integrated Links to their Trailers </h3>

With thw recommended movie list you also get the link of their respective official trailers on the poster itself 

<img width="1728" alt="image" src="https://github.com/nihitmittal/MovieRecommender/assets/52000096/373c6c51-56f4-4e0d-97f6-1876fe9c83fa">


<h2>Sources of the Datasets </h2>

[IMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/carolzhangdc/imdb-5000-movie-dataset)

[The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)

<h2>Delta </h2>

Refer to the Wiki page to know about the significant changes made as a part of Project 3 [here](https://github.com/nihitmittal/MovieRecommender/wiki/The-Delta-(Project-3))

<h2>Contributors </h2>

[Nihit Mittal](https://www.linkedin.com/in/nihitmittal/)

[Aryaman Jain](https://www.linkedin.com/in/aryaman-jain03/)

[Ankit Garg](https://www.linkedin.com/in/ankitgarg5/)
<h2>Contact Us </h2>

In case of any queries or issues please feel free to reach to us nmittal2@ncsu.edu 

<h2>Bug? 🐛</h2>
Raise a issue on this repository, we would love to look at it ❤️
  
## Contributions to the Project
Please refer to the [Contributing.md](https://github.com/raghavnarula/MovieRecommender/blob/master/CONTRIBUTING.md) if you want to contrbute to the Movie Recommender source code. Follow all the guidelines mentioned and raise a pull request for the developers to review before the code goes to the main source code.


Raise an issue on this repository, we would love to look at it ❤️
