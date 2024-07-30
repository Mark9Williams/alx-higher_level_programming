#!/usr/bin/node
// a script that computes the number of tasks completed by user id.

// 6-completed_tasks.js
const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.log('Usage: node 6-completed_tasks.js <API_URL>');
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

  const todos = JSON.parse(body);
  const userTasks = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (!userTasks[todo.userId]) {
        userTasks[todo.userId] = 0;
      }
      userTasks[todo.userId]++;
    }
  });

  // Remove users with 0 completed tasks
  for (const userId in userTasks) {
    if (userTasks[userId] > 0) {
      console.log(`${userId}: ${userTasks[userId]}`);
    }
  }
});
