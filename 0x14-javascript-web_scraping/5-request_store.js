#!/usr/bin/node
// a script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.log('Usage: node 5-request_store.js <URL> <file_path>');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status code:', response.statusCode);
    process.exit(1);
  }

  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error('Error writing to file:', err);
      process.exit(1);
    }

    console.log(`Data successfully written to ${filePath}`);
  });
});

