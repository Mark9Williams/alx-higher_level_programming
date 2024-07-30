#!/usr/bin/node
// a script that prints all characters of a Star Wars movie

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

  // Function to fetch and print character names in order
  const fetchCharacterNames = (urls, index = 0) => {
    if (index >= urls.length) return; // All characters have been processed

    request(urls[index], (error, response, body) => {
      if (error) {
        console.error('Error fetching character data:', error);
        fetchCharacterNames(urls, index + 1); // Continue with next character
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Failed to fetch character data. Status code:', response.statusCode);
        fetchCharacterNames(urls, index + 1); // Continue with next character
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);

      // Process next character
      fetchCharacterNames(urls, index + 1);
    });
  };

  fetchCharacterNames(characters);
});
