/* global $ */
// JavaScript script that fetches and lists the title for all movies

$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data) {
    // Iterate over the results and append each movie title to the list
    data.results.forEach(function (film) {
      $('#list_movies').append('<li>' + film.title + '</li>');
    });
  });
