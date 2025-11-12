#!usr/bin/node

fetch("https://hellosalut.stefanbohacek.com/?lang=fr")
.then(response => { return response.json() })
.then(data => {
  const h = data.hello
  const retrivedelement = document.getElementById("hello")
  retrivedelement.innerHTML = h
})
