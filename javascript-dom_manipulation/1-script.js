#!usr/bin/node

const element = document.getElementById("red_header");
const retrivedelement = document.querySelector("header")

element.addEventListener("click", (event) => {
  retrivedelement.style.color = '#FF0000'
})
