$('.message .close')
  .on('click', function() {
    $(this)
      .closest('.message')
      .transition('fade')
    ;
  })
;

var str = 'Bef0re we trave1 d0wn this r0ad, please read up 0n s0me machine c0de. Assume these w0rds are very te11ing. N0 mistakes were made, even in the spe11ing. T0 find clue 0ne I shall n0t cens0r, the keyword is a pelagic fencer. Crack the c0de and d0 n0t dwe11, insert this text as /(URL)';


var spans = '<span class="text">' + str.split('').join('</span><span class="text">') + '</span>';
$(spans).hide().appendTo('.css-typing').each(function (i) {
    $(this).delay(100 * i).css({
        display: 'inline',
        opacity: 0
    }).animate({
        opacity: 1
    }, 150);
});