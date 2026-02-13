const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");

hamburger.addEventListener("click", () => {
  navLinks.classList.toggle("show");
});

const dropdowns = document.querySelectorAll(".dropdown");

dropdowns.forEach(drop => {
  const btn = drop.querySelector(".dropbtn");
  btn.addEventListener("click", () => {
    drop.classList.toggle("open");
  });
});
