document.addEventListener('DOMContentLoaded', function () {
  const navbarLinks = document.querySelectorAll('.navbar-link');
  const sections = document.querySelectorAll('section'); // Sections de la page

  // Fonction pour vérifier si une section est dans la fenêtre visible
  function checkSectionInView() {
    sections.forEach(section => {
      const rect = section.getBoundingClientRect();
      const link = document.querySelector(`.navbar-link[href="#${section.id}"]`);
      
      // Si la section est visible à l'écran
      if (rect.top <= window.innerHeight && rect.bottom >= 0) {
        // Ajouter la classe 'active' au lien correspondant
        link.classList.add('active');
      } else {
        // Sinon, enlever la classe 'active'
        link.classList.remove('active');
      }
    });
  }

  // Vérification lors du défilement
  window.addEventListener('scroll', checkSectionInView);

  // Vérification initiale au chargement de la page
  checkSectionInView();

  // Ajouter un événement de clic à chaque lien
  navbarLinks.forEach(link => {
    link.addEventListener('click', function() {
      // Enlever la classe 'active' de tous les liens
      navbarLinks.forEach(link => link.classList.remove('active'));

      // Ajouter la classe 'active' au lien cliqué
      this.classList.add('active');
    });

    // Ajouter un événement de survol à chaque lien pour le surligner
    link.addEventListener('mouseover', function() {
      // Ajouter l'effet de survol (underline) sans ajouter de classe active
      this.classList.add('hover');
    });

    // Enlever l'effet de survol lorsqu'on sort du lien
    link.addEventListener('mouseleave', function() {
      // Enlever l'effet de survol (underline) lorsque la souris quitte le lien
      this.classList.remove('hover');
    });
  });
});
