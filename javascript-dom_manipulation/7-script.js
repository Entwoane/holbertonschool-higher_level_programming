function fetchTitle() {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  const ulHTML = document.getElementById('list_movies');

  fetch(url)
    .then((reponse) => {
      if (!reponse.ok) {
        throw new Error(`HTTP Error! Status: ${reponse.status}`);
      }
      return reponse.json();
    })
    .then((data) => {
      const results = data.results;
      ulHTML.innerHTML = '';
      results.forEach((film) => {
        const li = document.createElement('li');
        li.textContent = film.title;
        ulHTML.appendChild(li);
      });
    })
    .catch((error) => {
      console.error('Error fetching data:', error);
      ulHTML.innerHTML = '<li>Failed to load data</li>';
    });
}

fetchTitle();
