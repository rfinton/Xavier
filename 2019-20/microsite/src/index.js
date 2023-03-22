import { MDCSelect } from '@material/select';
import { MDCFormField } from '@material/form-field';
import { MDCRipple } from '@material/ripple';
import './main.scss';

const select = document.querySelectorAll( '.mdc-select' );

for( let i = 0; i < select.length; i++ ) {
  new MDCSelect( select[i] );
}

const buttonRipple = document.querySelectorAll( '.mdc-button' );

for( let i = 0; i < buttonRipple.length; i++ ) {
  new MDCRipple( buttonRipple[i] );
}

document.forms[0].addEventListener('submit', (evt) => {
  var form = document.forms[0];
  var form_values = {
    "networking": form['networking'].value,
    "innovating": form['innovating'].value,
    "thinking_analytically": form['thinking_analytically'].value,
    "accepting_and_acting_on_criticism": form['accepting_and_acting_on_criticism'].value,
    "creating_life_balance": form['creating_life_balance'].value,
  };

  form.reset();

  for( let x in form_values ) {
    switch( form_values[x] ) {
      case '1':
        form['rank_1'].value = x;
        break;
      case '2':
        form['rank_2'].value = x;
        break;
      case '3':
        form['rank_3'].value = x;
        break;
      default:
        continue;
    }
  }

  console.log( form['rank_1'].value );
  console.log( form['rank_2'].value );
  console.log( form['rank_3'].value );
});

window.addEventListener('load', () => {
  document.querySelector('.container').style.opacity = 1;
});