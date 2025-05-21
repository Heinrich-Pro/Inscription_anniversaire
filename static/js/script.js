const wrapper = document.querySelector('.wrapper');
const bthPopup = document.querySelector('.bthLogin-popup');
const iconClose = document.querySelector('.icon-close');

bthPopup.addEventListener('click', () => wrapper.classList.add('active-popup'));
iconClose.addEventListener('click', () => wrapper.classList.remove('active-popup'));