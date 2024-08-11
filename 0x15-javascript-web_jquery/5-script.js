/* global $ */

// Function to add a new <li> element to the list
$('#add_item').on('click', function () {
  const newItem = $('<li>').text('Item');

  // Append the new <li>
  $('.my_list').append(newItem);
});
