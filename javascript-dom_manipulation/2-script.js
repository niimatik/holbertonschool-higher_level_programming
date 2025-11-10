#!usr/bin/node

const element = document.getElementById("red_header");
const retrivedelement = document.querySelector("header")

element.addEventListener("click", (event) => {
  retrivedelement.classList.add("red")
})
