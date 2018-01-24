'use strict';

$(function () {
  $('.js-vote').click( function () {
    const url = $(this).data('url');
    var vote_count = $(this).siblings('.js-vote_count');
    $.ajax({
      type: 'get',
      url: url,
      dataType: 'json',
      async: true,
      success: function (data) {
        vote_count.text(data.vote_count);
      },
      error: function () {
        console.error('server error');
      }
    })
  });


  $('.js-answer_is_true').click( function () {
    const span = $(this);
    const url = span.data('url');
    $.ajax({
      type: 'get',
      url: url,
      dataType: 'json',
      async: true,
      success: function (data) {
        if(data.error == null){
            if(data.reset == true){
                span.removeClass('is_true');
            }
            else {
              $('.js-answer_is_true').removeClass('is_true');
              span.addClass('is_true');

            }
        }
        else {
            console.error(data.error)
        }

      },
      error: function () {
        console.error('server error');
      }
    })
  });
});

