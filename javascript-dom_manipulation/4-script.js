const addItem = document.getElementById('add_item');
const ulElement = document.querySelector('ul.my_list');

addItem.addEventListener('click', () => {
  const liElement = document.createElement('li');
  liElement.appendChild(document.createTextNode('Item'));
  ulElement.appendChild(liElement);
});
