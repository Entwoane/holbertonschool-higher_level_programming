document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  const helloElement = document.getElementById('hello');

  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      helloElement.textContent = data.hello;
    })
    .catch((error) => {
      console.error('Error fetching data:', error);
      helloElement.textContent = 'Failed to load translation';
    });
});
