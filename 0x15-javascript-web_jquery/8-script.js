$.get("https://swapi-api.hbtn.io/api/films/?format=json", function (data) {
  $.each(data.results, function (i, film) {
   $("#list_movies").append('<li>' + film.title + '</li>');
  });
});
