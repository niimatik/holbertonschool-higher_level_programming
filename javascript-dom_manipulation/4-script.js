#!usr/bin/node

const element = document.getElementById("add_item");
const retrivedelement = document.querySelector("ul");

element.addEventListener("click", function () {
  const item = document.createElement("li");
  item.textContent = "Item";
  retrivedelement.appendChild(item);
});
