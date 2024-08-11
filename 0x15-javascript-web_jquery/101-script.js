/* global $ */
$(document).ready(function () {
  // Add a new item to the list when DIv#add_item is clicked
  $('#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });

  // Remove the last item from the list when DIV#remove_item is clicked
  $('#remove_item').click(function () {
    $('.my_list li:last-child').remove();
  });

  // clear all items from list when DIV#clear_list is clicked
  $('#clear_list').click(function () {
    $('.my_list').empty();
  });
});
