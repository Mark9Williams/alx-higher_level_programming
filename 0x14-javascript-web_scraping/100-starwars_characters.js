#!/usr/bin/node
//  a script that prints all characters of a Star Wars movie

// 7-starwars_characters.js
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: node 7-starwars_characters.js <movie_id>');
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
  const characters = film.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error fetching character data:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Failed to fetch character data. Status code:', 
			response.statusCode);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
