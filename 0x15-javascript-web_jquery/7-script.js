$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', leiaName => {
  $('DIV#character').html(leiaName.name);
});
