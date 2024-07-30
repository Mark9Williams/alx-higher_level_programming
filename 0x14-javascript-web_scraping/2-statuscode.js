#!/usr/bin/node
//A script that display the status code of a GET request.

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: node 2-statuscode.js <URL>');
  process.exit(1);
}

const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.error('Error:', error); // Print the error if one occurred
  } else {
    console.log(`code: ${response.statusCode}`); // Print the response status code
  }
});

