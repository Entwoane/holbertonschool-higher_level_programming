const redClass = document.getElementById('red_header');
const header = document.querySelector('header');

redClass.addEventListener('click', () => {
  header.classList.add('red');
});
