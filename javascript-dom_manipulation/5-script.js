#!usr/bin/node

const element = document.getElementById("update_header");
const retrivedelement = document.querySelector("header")

element.addEventListener("click", function () {
  retrivedelement.textContent = "New Header!!!";
});
