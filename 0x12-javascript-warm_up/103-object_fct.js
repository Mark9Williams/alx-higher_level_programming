#!/usr/bin/node
// a script that adds a new function incr that increments the integer value

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

/* Adding the incr function to mybject */
myObject.incr = function () {
  this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
