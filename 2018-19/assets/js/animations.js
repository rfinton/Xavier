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
  try {
    if(purl) {
      //setCK(purl, '.ready.xula.edu/tattoo.html');
    }
  } catch(e) {
    console.log(e);
  }
  
  $('div.x-checkbox').eq(4).attr('title', 'If I could master knowing when to say \"enough\", I would be happier.');
  
  // targeting old Android stock browsers which don't support vw or vh units
  if(navigator.userAgent.search(/linux; u;/i) != -1) {
    var xlogo = document.querySelector('.x-logo');
    $('img.x-logo').css('width', $(window).width() * 0.7 + 'px');
    $('div.logo').css('height', ($(window).width() * 0.7) / 1.3513 + 'px');

    if(location.href.search(/thanks/) != -1) {
      $('div.logo').css({display:'inline-flex',opacity:1});
    }
  }

  // Set up some CSS
  $('#h1a').css('font-size', $(window).height() * 0.04 + 'px');
  $('#h1b h1').css('font-size', $(window).height() * 0.03 + 'px');
  $('.xli').css('font-size', $(window).height() * 0.023 + 'px');
  $('.thin-gold-line').css('width', '0px');

  // Velocity animations begin here.
  if(location.href.search(/Xavier/) != -1) {
    /*
    setTimeout(function() {
      // mobile device detection
      if(typeof(window.orientation) != 'undefined' || navigator.userAgent.search(/iemobile/i) != -1) {
        $('[data-toggle="tooltip"]').tooltip({trigger: 'focus'});
        requestAnimationFrame(function() {
          $('.foreground').velocity('fadeIn', {delay:500, duration:1500});
          $('.logo').velocity({opacity: [1,0], translateY: [-10,-30]}, {delay:2000, duration:1500});
          $('.thin-gold-line').velocity({width: [$('img.x-logo').outerWidth(),0]}, {delay:3500, duration:1000});
          $('.view-1, .xbutton').velocity('transition.slideUpIn', {delay:4500, duration:1000});
        });
      } else {
        $('[data-toggle="tooltip"]').tooltip({trigger: 'hover', placement: 'auto left'});
        requestAnimationFrame(function() {
          $('.photos-left').css('display', 'inline-block');
          $('.photos-right').css('display', 'inline-block');
          $('.photos-left').velocity({opacity: [1,0], translateX: [0,30]}, {delay:500, duration:1000});
          $('.photos-right').velocity({opacity: [1,0], translateX: [0,-30]}, {delay:500, duration:1000});
          $('.foreground').velocity('fadeIn', {delay:1500, duration:1500});
          $('.logo').velocity({opacity: [1,0], translateY: [-10,-50]}, {delay:1000, duration:1500});
          $('.thin-gold-line').velocity({width: [$('img.x-logo').outerWidth(),0]}, {delay:2000, duration:1000});
          $('.view-1, .xbutton').velocity('transition.slideUpIn', {delay:2500, duration:1000});
        });
      }
    }, 1500);
    */
  }

  if(location.href.search(/thanks/) != -1) {
    $('.photos-left').css('display', 'inline-block');
    $('.photos-right').css('display', 'inline-block');
    $('.photos-left').css({opacity: 1, transform: 'translateX(0px)'});
    $('.photos-right').css({opacity: 1, transform: 'translateX(0px)'});
    $('.foreground').css('display', 'block');
    $('.logo, .thank-you').css({opacity:1});
    $('.thin-gold-line').css('width', $('img.x-logo').outerWidth() + 'px');
    $('.xbutton').css({opacity:1});
  }

  if(location.href.search(/adclick/) != -1) {
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
      } else {
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
    }, 1500);
  }
};


// targeting mobile devices
window.addEventListener('orientationchange', function() {
  if(location.href.search(/index|adclick/) != -1) {
    $('.photos-left').velocity({opacity: [1,0], translateX: [0,30]}, {duration:1000});
    $('.photos-right').velocity({opacity: [1,0], translateX: [0,-30]}, {duration:1000});
  }
});

// targeting mobile devices
window.onscroll = function() {
  if(location.href.search(/adclick/) != -1) {
    if(typeof(window.orientation) != 'undefined' || navigator.userAgent.search(/iemobile/i) != -1) {
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
    }
  }
};
