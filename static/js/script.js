// Navigation scroll effect
    window.addEventListener('scroll', function() {
      const navbar = document.getElementById('navbar');
      if (window.scrollY > 30) {
        navbar.classList.add('nav-scrolled');
      } else {
        navbar.classList.remove('nav-scrolled');
      }
      
      // Reveal animations
      const reveals = document.querySelectorAll('.reveal');
      const windowHeight = window.innerHeight;
      const revealPoint = 100;
      
      reveals.forEach(element => {
        const revealTop = element.getBoundingClientRect().top;
        if (revealTop < windowHeight - revealPoint) {
          element.classList.add('in-view');
        }
      });
      
      // Section title underline animation
      const sectionTitles = document.querySelectorAll('.section-title');
      sectionTitles.forEach(title => {
        const titleTop = title.getBoundingClientRect().top;
        if (titleTop < windowHeight - 80) {
          title.classList.add('in-view');
        }
      });
      
      // Navigation highlighting
      const sections = document.querySelectorAll('section[id]');
      const navLinks = document.querySelectorAll('.nav-link');
      
      let current = '';
      const scrollY = window.pageYOffset + 100;
      
      sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        
        if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
          current = section.getAttribute('id');
        }
      });
      
      navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}` || 
            (current === '' && link.getAttribute('href') === '#home')) {
          link.classList.add('active');
        }
      });
    });
    
    // Smooth scroll for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;
        
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
          window.scrollTo({
            top: targetElement.offsetTop - 80,
            behavior: 'smooth'
          });
          
          // Update active state
          document.querySelectorAll('.nav-link').forEach(link => link.classList.remove('active'));
          this.classList.add('active');
        }
      });
    });
    
    // Language toggle functionality
    const langButtons = document.querySelectorAll('.lang-btn');
    langButtons.forEach(button => {
      button.addEventListener('click', function() {
        langButtons.forEach(btn => btn.classList.remove('active'));
        this.classList.add('active');
        
        // Here you would typically load translations
        // For this demo, we'll just toggle some text
        if (this.textContent === 'FR') {
          document.querySelector('.punchline-text').textContent = 
            "...";
          document.querySelector('.identity-statement').textContent = 
            "Odoo Python Developer";
          document.querySelector('.hero-bio').textContent = 
            "";
        } else {
          document.querySelector('.punchline-text').textContent = 
            "";
          document.querySelector('.identity-statement').textContent = 
            "Odoo Python Developer";
          document.querySelector('.hero-bio').textContent = 
            "";
        }
      });
    });
    
    // Initial animations
    document.addEventListener('DOMContentLoaded', function() {
      // Trigger initial scroll for animations
      setTimeout(() => {
        window.dispatchEvent(new Event('scroll'));
      }, 100);
      
      // Add hover effect to project cards
      const projectCards = document.querySelectorAll('.project-card');
      projectCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
          this.style.transform = 'translateY(-8px)';
        });
        
        card.addEventListener('mouseleave', function() {
          this.style.transform = 'translateY(-5px)';
        });
      });
    });


    // Back to top button functionality
const backToTopButton = document.getElementById('backToTop');

window.addEventListener('scroll', function() {
  // Existing scroll code...
  
  // Show back-to-top button after scrolling down 300px
  if (window.scrollY > 300) {
    backToTopButton.classList.add('visible');
  } else {
    backToTopButton.classList.remove('visible');
  }
});

// Smooth scroll to top when clicked
backToTopButton.addEventListener('click', function(e) {
  e.preventDefault();
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
  
  // Update active state in navbar
  document.querySelectorAll('.nav-link').forEach(link => link.classList.remove('active'));
  document.querySelector('a[href="#home"]').classList.add('active');
});


// Menu mobile functionality
const mobileToggle = document.getElementById('mobileToggle');
const navLinks = document.getElementById('navLinks');
const navOverlay = document.getElementById('navOverlay');

if (mobileToggle && navLinks) {
  // Ouvrir/fermer le menu mobile
  mobileToggle.addEventListener('click', (e) => {
    e.stopPropagation();
    navLinks.classList.toggle('active');
    navOverlay.classList.toggle('active');
    // Changer l'icône
    const icon = mobileToggle.querySelector('i');
    if (navLinks.classList.contains('active')) {
      icon.classList.remove('fa-bars');
      icon.classList.add('fa-times');
      document.body.style.overflow = 'hidden'; // Empêcher le scroll
    } else {
      icon.classList.remove('fa-times');
      icon.classList.add('fa-bars');
      document.body.style.overflow = ''; // Réactiver le scroll
    }
  });

  // Fermer le menu en cliquant sur l'overlay
  navOverlay.addEventListener('click', () => {
    navLinks.classList.remove('active');
    navOverlay.classList.remove('active');
    mobileToggle.querySelector('i').classList.remove('fa-times');
    mobileToggle.querySelector('i').classList.add('fa-bars');
    document.body.style.overflow = '';
  });

  // Fermer le menu en cliquant sur un lien
  document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('active');
      navOverlay.classList.remove('active');
      mobileToggle.querySelector('i').classList.remove('fa-times');
      mobileToggle.querySelector('i').classList.add('fa-bars');
      document.body.style.overflow = '';
    });
  });

  // Fermer le menu en appuyant sur Échap
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      navLinks.classList.remove('active');
      navOverlay.classList.remove('active');
      mobileToggle.querySelector('i').classList.remove('fa-times');
      mobileToggle.querySelector('i').classList.add('fa-bars');
      document.body.style.overflow = '';
    }
  });
}