#!usr/bin/node

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
.then(response => { return response.json() })
.then(data => {
  const films = data.results;
  const retrivedelement = document.getElementById("list_movies");
  films.forEach(element => {
    const li = document.createElement("li");
    li.textContent = element.title;
    retrivedelement.appendChild(li);
  });
})
