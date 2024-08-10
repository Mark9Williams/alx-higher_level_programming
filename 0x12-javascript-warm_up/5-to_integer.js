#!/usr/bin/node
// prints the first argument if it can be converted to an integer
const args = process.argv.slice(2);
const num = parseInt(args[0], 10);
if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
