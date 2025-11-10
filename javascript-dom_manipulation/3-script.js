#!usr/bin/node

const element = document.getElementById("toggle_header");
const retrivedelement = document.querySelector("header")

element.addEventListener("click", (event) => {
  if (retrivedelement.classList.contains('red')) {
    retrivedelement.classList.remove('red');
    retrivedelement.classList.add('green');
  } else if (retrivedelement.classList.contains('green')) {
    retrivedelement.classList.remove('green');
    retrivedelement.classList.add('red');
  }
})
