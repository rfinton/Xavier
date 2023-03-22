var li2 = $('.xli-2');
var li3 = $('.xli-3');
li2.opaque = false;
li3.opaque = false;
window.scrollCounter = 0;

function isVisible($el) {
  var winTop = $(window).scrollTop();
  var winBottom = winTop + $(window).height();
  var elTop = $el.offset().top;
  var elBottom = elTop + $el.height();
  return elTop <= winBottom;
}

window.onload = function() {
  // targeting old Android stock browsers which don't support vw or vh units
  if(navigator.userAgent.search(/linux; u;/i) != -1) {
    var xlogo = document.querySelector('.x-logo');
    $('img.x-logo').css('width', $(window).width() * 0.7 + 'px');
    $('div.logo').css('height', ($(window).width() * 0.7) / 1.3513 + 'px');
  }

  // Set up some CSS
  $('#h1a').css('font-size', $(window).height() * 0.04 + 'px');
  $('#h1b h1').css('font-size', $(window).height() * 0.03 + 'px');
  $('.xli').css('font-size', $(window).height() * 0.023 + 'px');
  $('.thin-gold-line').css('width', '0px');

  window.onscroll = function() {
    ++scrollCounter;

    if(scrollCounter % 24 == 0) {
      if(isVisible(li2)) {
        if(!li2.opaque) {
          li2.opaque = true;
          li2.velocity('transition.slideUpIn', {duration:2000});
        }
      } else {
        li2.opaque = false;
      }

      if(isVisible(li3)) {
        if(!li3.opaque) {
          li3.opaque = true;
          li3.velocity('transition.slideUpIn', {duration:2000});
        }
      } else {
        li3.opaque = false;
      }
    }
  };

  window.addEventListener('orientationchange', function() {
    if(location.href.search(/index|adclick/) != -1) {
      $('.photos-left').velocity({opacity: [1,0], translateX: [0,30]}, {duration:1000});
      $('.photos-right').velocity({opacity: [1,0], translateX: [0,-30]}, {duration:1000});
    }
  });

  setTimeout(function() {
    // mobile device detection
    if(typeof(window.orientation) != 'undefined' || navigator.userAgent.search(/iemobile/i) != -1) {
      requestAnimationFrame(function() {
        $('.foreground').velocity('fadeIn', {delay:500, duration:1500});
        $('div.logo').velocity({opacity: [1,0], translateY: [-10,-30]}, {delay:2000, duration:1500});
        $('.thin-gold-line').velocity({width: [$('img.x-logo').outerWidth(),0]}, {delay:3500, duration:1000});
        $('#h1b').velocity('fadeIn', {delay:4500, duration:1500});
        $('.view-1, .xbutton, .xli-1').velocity('transition.slideUpIn', {delay:5000, duration:1000});
      });
    }
    // desktop machines
    else {
      requestAnimationFrame(function() {
        $('.photos-left').css('display', 'inline-block');
        $('.photos-right').css('display', 'inline-block');
        $('.photos-left').velocity({opacity: [1,0], translateX: [0,30], translateZ: [0,0]}, {delay:500});
        $('.photos-right').velocity({opacity: [1,0], translateX: [0,-30], translateZ: [0,0]}, {delay:500});
        $('.foreground').velocity('fadeIn');
        $('.logo').velocity({opacity: [1,0], translateY: [-10,-60], translateZ: [0,0]}, {delay:1000, duration:700});
        $('.thin-gold-line').velocity({width: [$('img.x-logo').outerWidth(),0]}, {delay:1000, duration:700});
        $('.view-1').velocity('transition.slideUpIn', {delay:1500, duration:700, complete: function() {
          $('.xli').velocity('transition.slideUpIn', {stagger:250, complete: function() {
            $('.cta, .xbutton').velocity({opacity: [1,0], translateY: [0,20]});
          }});
        }});
      });
    }
  }, 500);
};