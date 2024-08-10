#!/usr/bin/node
// a script that prints x times “C is fun”

const args = process.argv.slice(2);
const x = parseInt(args[0], 10);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
