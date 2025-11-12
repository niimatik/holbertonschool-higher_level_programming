#!usr/bin/node

fetch("https://swapi-api.hbtn.io/api/people/4/?format=json")
.then(response => { return response.json() })
.then(data => {
  const character = data.name
  const retrivedelement = document.getElementById("character")
  retrivedelement.innerHTML = character
})
