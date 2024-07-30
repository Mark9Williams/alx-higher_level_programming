#!/usr/bin/node
// a script that prints the number of movies where the character
// “Wedge Antilles” is present.

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.log('Please provide the API URL.');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status code:', response.statusCode);
    process.exit(1);
  }

  const films = JSON.parse(body).results;
  let count = 0;

  films.forEach(film => {
    if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  });

  console.log(count);
});
