$('.message .close')
  .on('click', function() {
    $(this)
      .closest('.message')
      .transition('fade')
    ;
  })
;

var str = 'Before we travel down this road, please read up on some machine code. Assume theses words are very telling. No mistakes were made, even in the spelling. To find clue 1 I shall not censor, the keyphrase is a pelagic fencer. Crack the code but do not dwell, insert this text as /(URL)';


var spans = '<span class="text">' + str.split('').join('</span><span class="text">') + '</span>';
$(spans).hide().appendTo('.css-typing').each(function (i) {
    $(this).delay(10 * i).css({
        display: 'inline',
        opacity: 0
    }).animate({
        opacity: 1
    }, 150);
});