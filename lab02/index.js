// Smooth scroll
function scrollToSection(id) {
    document.getElementById(id).scrollIntoView({ behavior: "smooth" });
  }
  
  // Toggle dark/light theme
  function toggleTheme() {
    document.body.classList.toggle("dark");
  }
  