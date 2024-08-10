#!/usr/bin/node
// Write a function that increments and calls a function.

function addMeMaybe (number, theFunction) {
  number++;
  theFunction(number);
}

// making it visible from outside
module.exports = {
  addMeMaybe
};
