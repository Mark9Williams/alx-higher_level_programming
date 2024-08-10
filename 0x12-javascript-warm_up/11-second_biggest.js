#!/usr/bin/node
// a script that finds the second biggest integer from the list of arguments

const args = process.argv.slice(2).map(Number);

// Function to find the second largest number
function findSecondBiggest (numbers) {
  if (numbers.length < 2) {
    return 0;
  }

  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (const num of numbers) {
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num < largest) {
      secondLargest = num;
    }
  }

  return secondLargest === -Infinity ? 0 : secondLargest;
}

console.log(findSecondBiggest(args));
