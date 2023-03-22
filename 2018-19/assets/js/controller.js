function removeStar() {
  var deadline = new Date('11/6/2018');
  var today = new Date();

  if(today >= deadline) {
    var star = document.getElementById('starburst');
    star.style.display = 'none';
  }
}

function getRanks(ev) {
  ev.target.style.background = '#939393';
  document.querySelector('.visit-xula').disabled = true;
  document.querySelector('.ready-btn').disabled = true;

  var rank1 = false;
  var rank2 = false;
  var rank3 = false;
  var select = document.querySelectorAll('select');

  for (var s = 0; s < 5; s++) {
    console.log(select[s].selectedIndex);
    if(select[s].selectedIndex != 0) {
      switch(select[s].selectedIndex) {
        case 1:
          document.forms[0]['rank1'].value = select[s].dataset.obj;
          rank1 = true;
          break;
        case 2:
          document.forms[0]['rank2'].value = select[s].dataset.obj;
          rank2 = true;
          break;
        case 3:
          document.forms[0]['rank3'].value = select[s].dataset.obj;
          rank3 = true;
          break;
      }
    }
  }

  if(!rank1 || !rank2 || !rank3) {
    alert('You forgot to assign a ranking for your top 3 choices.')
    $('.load-spinner').velocity('stop');
    $('.load-spinner').velocity('transition.slideDownOut');
    ev.target.style.background = '#ffc627';
    document.querySelector('.visit-xula').disabled = false;
    document.querySelector('.ready-btn').disabled = false;
    return false;
  }

  return true
}

function initEventHandlers() {
  $('.ready-btn').click(function(ev) {
    $('.load-spinner').velocity('transition.slideUpIn');
    if(getRanks(ev)) {
      document.forms[0]['submitaction'].value = 'I\'m ready.';
      setTimeout(function() {
        document.forms[0].submit();
      }, 1000);
    }
  });
  
  $('.visit-xula').click(function(ev) {
    $('.load-spinner').velocity('transition.slideUpIn');
    document.forms[0]['submitaction'].value = 'I\'d like to visit XULA.';
    setTimeout(function() {
      document.forms[0].submit();
      window.open('http://www.xula.edu/admissions/campustour.html', '_blank');
    }, 1000);
  });
}

$(document).ready(function() {
  initEventHandlers();
  removeStar();
});