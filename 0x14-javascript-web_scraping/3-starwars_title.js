#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode 
// number matches a given integer.

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a movie ID.');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status code:', response.statusCode);
    process.exit(1);
  }

  const film = JSON.parse(body);
  console.log(film.title);
});

