const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, data => {
  for (let i = 0; i < data.count; i++) {
    $('ul#list_movies').append('<li>' + data.results[i].title + '</li>');
  }
});
