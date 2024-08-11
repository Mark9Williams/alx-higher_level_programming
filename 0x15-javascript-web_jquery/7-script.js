/* global $ */

// Function to fetch and display the character name
$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json',
  function (data) {
    $('#character').text(data.name);
  });
