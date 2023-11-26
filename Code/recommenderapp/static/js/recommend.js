$(function () {
    // Button will be disabled until we type anything inside the input field
    const source = document.getElementById('autoComplete');
    const inputHandler = function (e) {
      if (e.target.value == "") {
        $('.movie-button').attr('disabled', true);
      }
      else {
        $('.movie-button').attr('disabled', false);
      }
    }
    source.addEventListener('input', inputHandler);
  
    $('.movie-button').on('click', function () {
      var my_api_key = 'c2dc5ac6d552dd25bfd3f4f156445c2e';
      var title = $('.movie').val();
      if (title == "") {
        $('.results').css('display', 'none');
        $('.fail').css('display', 'block');
      }
      else {
        load_details(my_api_key, title);
      }
    });
  });
  
  // will be invoked when clicking on the recommended movies
  function recommendcard(e) {
    var my_api_key = 'c2dc5ac6d552dd25bfd3f4f156445c2e';
    var title = e.getAttribute('title');
    load_details(my_api_key, title);
  }
  
  // get the basic details of the movie from the API (based on the name of the movie)
  function load_details(my_api_key, title) {
    $.ajax({
      type: 'GET',
      url: 'https://api.themoviedb.org/3/search/movie?api_key=' + my_api_key + '&query=' + title,
  
      success: function (movie) {
        if (movie.results.length < 1) {
          $('.fail').css('display', 'block');
          $('.results').css('display', 'none');
          $("#loader").delay(500).fadeOut();
        }
        else {
          $("#loader").fadeIn();
          $('.fail').css('display', 'none');
          $('.results').delay(1000).css('display', 'block');
          var movie_id = movie.results[0].id;
          var movie_title = movie.results[0].original_title;
          movie_recs(movie_title, movie_id, my_api_key);
        }
      },
      error: function () {
        alert('Invalid Request');
        $("#loader").delay(500).fadeOut();
      },
    });
  }
  
  // passing the movie name to get the similar movies from python's flask
  function movie_recs(movie_title, movie_id, my_api_key) {
    $.ajax({
      type: 'POST',
      url: "/similarity",
      data: { 'name': movie_title },
      success: function (recs) {
        if (recs == "Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies") {
          $('.fail').css('display', 'block');
          $('.results').css('display', 'none');
          $("#loader").delay(500).fadeOut();
        }
        else {
          $('.fail').css('display', 'none');
          $('.results').css('display', 'block');
          var movie_arr = recs.split('---');
          var arr = [];
          for (const movie in movie_arr) {
            arr.push(movie_arr[movie]);
          }
          get_movie_details(movie_id, my_api_key, arr, movie_title);
        }
      },
      error: function () {
        alert("error recs");
        $("#loader").delay(500).fadeOut();
      },
    });
  }
  
  // get all the details of the movie using the movie id.
  function get_movie_details(movie_id, my_api_key, arr, movie_title) {
    $.ajax({
      type: 'GET',
      url: 'https://api.themoviedb.org/3/movie/' + movie_id + '?api_key=' + my_api_key,
      success: function (movie_details) {
        show_details(movie_details, arr, movie_title, my_api_key, movie_id);
      },
      error: function () {
        alert("API Error!");
        $("#loader").delay(500).fadeOut();
      },
    });
  }
  
  // passing all the details to python's flask for displaying and scraping the movie reviews using imdb id
  function show_details(movie_details, arr, movie_title, my_api_key, movie_id) {
    var imdb_id = movie_details.imdb_id;
    var overview = movie_details.overview;
    var genres = movie_details.genres;
    var rating = movie_details.vote_average;
    var vote_count = movie_details.vote_count;
    var release_date = new Date(movie_details.release_date);
    var runtime = parseInt(movie_details.runtime);
    var status = movie_details.status;
    var genre_list = []
    for (var genre in genres) {
      genre_list.push(genres[genre].name);
    }
    var my_genre = genre_list.join(", ");
    if (runtime % 60 == 0) {
      runtime = Math.floor(runtime / 60) + " hour(s)"
    }
    else {
      runtime = Math.floor(runtime / 60) + " hour(s) " + (runtime % 60) + " min(s)"
    }
  
    // Fetch trailer information using the YouTube Data API
    $.ajax({
      type: 'GET',
      url: 'https://www.googleapis.com/youtube/v3/search',
      data: {
        q: movie_title + ' official trailer',
        part: 'snippet',
        type: 'video',
        maxResults: 1,
        key: 'AIzaSyDsXp1rAboUy-e1kYviXO89mXoO4GT_Yag', // Replace with your YouTube API key
      },
      success: function (youtubeData) {
        var trailerKey = youtubeData.items.length > 0 ? youtubeData.items[0].id.videoId : null;
        yt_link = trailerKey ? 'https://www.youtube.com/watch?v=' + trailerKey : null;
        console.log(yt_link);
        // Continue with the existing code to send details to Python's Flask
        details = {
          'title': movie_title,
          'imdb_id': imdb_id,
          'genres': my_genre,
          'overview': overview,
          'rating': rating,
          'vote_count': vote_count.toLocaleString(),
          'release_date': release_date.toDateString().split(' ').slice(1).join(' '),
          'runtime': runtime,
          'status': status,
          'rec_movies': JSON.stringify(arr),
          'trailer': yt_link,  // Add the trailer link to the details object
        };
  
        $.ajax({
          type: 'POST',
          data: details,
          url: "/recommend",
          dataType: 'html',
          complete: function () {
            $("#loader").delay(500).fadeOut();
          },
          success: function (response) {
            $('.results').html(response);
            $('#autoComplete').val('');
            $(window).scrollTop(0);
          }
        });
      },
      error: function () {
        alert("Error fetching trailer information from YouTube");
        $("#loader").delay(500).fadeOut();
      },
    });
  }
  
  function Trailercard(e) {
    var title = e.getAttribute('title');
    $.ajax({
      type: 'GET',
      url: 'https://www.googleapis.com/youtube/v3/search',
      data: {
        q: title + ' official trailer',
        part: 'snippet',
        type: 'video',
        maxResults: 1,
        key: 'AIzaSyDsXp1rAboUy-e1kYviXO89mXoO4GT_Yag', // Replace with your YouTube API key
      },
      success: function (youtubeData) {
        var trailerKey = youtubeData.items.length > 0 ? youtubeData.items[0].id.videoId : null;
        yt_link = trailerKey ? 'https://www.youtube.com/watch?v=' + trailerKey : null;
        window.open(yt_link, "_blank");
      },
      error: function () {
        alert("Error fetching trailer information from YouTube");
        $("#loader").delay(500).fadeOut();
      },
    });
  }
  