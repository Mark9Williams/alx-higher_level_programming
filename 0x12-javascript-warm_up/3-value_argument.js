#!/usr/bin/node
// a script that prints the first argument passed to it
const args = process.argv.slice(2);
if (args[0] !== undefined) {
  console.log(args[0]);
} else {
  console.log('No argument');
}
