function fetchName() {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  const html = document.getElementById('character');

  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      const name = data.name;
      html.textContent = name;
    })
    .catch((error) => {
      console.error('Error fetching data:', error);
      html.textContent = 'Failed to load data';
    });
}

fetchName();
