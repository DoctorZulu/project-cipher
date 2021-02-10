

$('.message .close')
  .on('click', function () {
    $(this)
      .closest('.message')
      .transition('fade');
  });

  /* tons of examples referenced https://css-tricks.com/snippets/css/typewriter-effect/, 
  https://www.codesdope.com/blog/article/12-creative-css-and-javascript-text-typing-animati/*/

var str = 'Bef0re we trave1 d0wn this r0ad, please read up 0n s0me machine c0de. Assume these w0rds are very te11ing. N0 mistakes were made, even in the spe11ing. T0 find clue 0ne I shall n0t cens0r, the keyword is a pelagic fencer. Crack the c0de and d0 n0t dwe11, insert this text as /(URL)';

/* with delay appending each character as spans, opacity is animated for typewriter effect */
var spans = '<span class="text">' + str.split('').join('</span><span class="text">') + '</span>';
$(spans).hide().appendTo('.css-typing').each(function (i) {
  $(this).delay(90 * i).css({
    display: 'inline',
    opacity: 0
  }).animate({
    opacity: 1
  }, 100);
});

var str1 = '"Do not go gentle into that good night, Old age should burn and rave at close of day; Rage, rage against the dying of the light. Though wise men at their end know dark is right, Because their words had forked no lightning they Do not go gentle into that good night. Good men, the last wave by, crying how bright Their frail deeds might have danced in a green bay, Rage, rage against the dying of the light. Wild men who caught and sang the sun in flight, And learn, too late, they grieved it on its way, Do not go gentle into that good night. Grave men, near death, who see with blinding sight Blind eyes could blaze like meteors and be gay, Rage, rage against the dying of the light. And you, my father, there on the sad height, Curse, bless, me now with your fierce tears, I pray. Do not go gentle into that good night. Rage, rage against the dying of the light"'

var spans = '<span class="text">' + str1.split('').join('</span><span class="text">') + '</span>';
$(spans).hide().appendTo('.css-typing1').each(function (i) {
  $(this).delay(90 * i).css({
    display: 'inline',
    opacity: 0
  }).animate({
    opacity: 1
  }, 100);
});

var str2 = "Aren't you a smart cookie? You've made it this far, but I'm having too much fun. You complete me.... I think I'll hang on to this website a little longer. P.S. thanks for giving me your admin credentials earlier. Those should come in handy."

var spans = '<span class="text">' + str2.split('').join('</span><span class="text">') + '</span>';
$(spans).hide().appendTo('.css-typing2').each(function (i) {
  $(this).delay(90 * i).css({
    display: 'inline',
    opacity: 0
  }).animate({
    opacity: 1
  }, 100);
});


/* Inspired by Julius Caesar and article/examples by Prashant Yadav on Learersbucket.com/examples/algorithms/caesar-cipher-in-javascript */

let caesarShift = function (str, shift) {

  if (shift < 0) {
    return caesarShift(str, shift + 26);
  }


  let output = "";
  for (let i = 0; i < str.length; i++) {
    let c = str[i];
    /* Checking for letters */
    if (c.match(/[a-z]/i)) {
      /* checking character code for upper/lower */
      let code = str.charCodeAt(i);
      /* handling upper */
      if (code >= 65 && code <= 90) {
        c = String.fromCharCode(((code - 65 + shift) % 26) + 65);
      }
      /* handling lower */
      else if (code >= 97 && code <= 122) {
        c = String.fromCharCode(((code - 97 + shift) % 26) + 97);
      }
    }
    output += c;
  }
  return output;
};

console.log("Well look at you, you know how to access the dev-tools. While you are here, feel free to use the Caesar shift encoder I scripted, simply invoke caesarShift(phrase, numberofshifts)")