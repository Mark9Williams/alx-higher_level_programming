/* global $ */
$(document).ready(function () {
  function fetchHello () {
    const langCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;

    $.get(apiUrl, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(function () {
    fetchHello();
  });

  $('#language_code').keypress(function (e) {
    if (e.which === 13) { // 13 is the Enter key code
      fetchHello();
    }
  });
});
