#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length < 4) {
  console.error('Usage: ./writeToFile.js <file-path> <string-to-write>');
  process.exit(1);
}

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the file using UTF-8 encoding
fs.writeFile(filePath, stringToWrite + '\n', 'utf8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
});

