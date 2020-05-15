$(document).ready(function () {
    $('div#toggle_header').on('click', function () {
      /*
        we can use only toggleClass
      */
      if ($('header').hasClass('red')) {
        $('header').removeClass('red');
        $('header').addClass('green');
      } else if ($('header').hasClass('green')) {
        $('header').removeClass('green');
        $('header').addClass('red');
      }
    });
  });
