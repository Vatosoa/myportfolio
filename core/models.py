from django.db import models
from django.utils.translation import gettext_lazy as _

class CVFile(models.Model):
    """Gestion dynamique des fichiers CV par langue"""
    LANGUAGE_CHOICES = [
        ('fr', 'Français'),
        ('en', 'English'),
    ]
    
    language = models.CharField(_("Langue"), max_length=10, choices=LANGUAGE_CHOICES, default='fr')
    title = models.CharField(_("Titre du CV"), max_length=100, default="CV")
    pdf_file = models.FileField(_("Fichier PDF"), upload_to='cv/')
    is_active = models.BooleanField(_("Actif"), default=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("Fichier CV")
        verbose_name_plural = _("Fichiers CV")
        unique_together = ['language']
    
    def __str__(self):
        return f"CV - {self.get_language_display()}"
        
class AboutContent(models.Model):
    """Contenu dynamique pour la section About"""
    LANGUAGE_CHOICES = [
        ('fr', 'Français'),
        ('en', 'English'),
    ]
    
    language = models.CharField(_("Langue"), max_length=10, choices=LANGUAGE_CHOICES, default='fr')
    
    # Sections du About
    professional_summary = models.TextField(_("Résumé professionnel"))
    education = models.TextField(_("Formation"))
    volunteer_work = models.TextField(_("Bénévolat"))
    personal_qualities = models.TextField(_("Qualités personnelles"))
    
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("Contenu About")
        verbose_name_plural = _("Contenus About")
        unique_together = ['language']
    
    def __str__(self):
        return f"About - {self.get_language_display()}"

class Project(models.Model):
    PROJECT_TYPES = [
        ('ODOO', 'Développement Odoo'),
        ('IA', 'Recherche IA'),
        ('FULL', 'Projet Full-Stack'),
        ('ACADEMIC', 'Projet Académique'),
    ]
    
    title = models.CharField(_("Titre"), max_length=200)
    slug = models.SlugField(_("Slug"), unique=True)
    project_type = models.CharField(_("Type de projet"), max_length=10, choices=PROJECT_TYPES)
    
    # Pilier 3 : Récit par cas d'étude - PARFAIT pour votre profil
    challenge = models.TextField(_("Défi/Contexte"))
    solution = models.TextField(_("Solution technique")) 
    result = models.TextField(_("Résultats/Impact"))
    
    # Spécifique à votre expertise
    technologies = models.CharField(_("Stack technique"), max_length=300)
    odoo_modules = models.CharField(_("Modules Odoo"), max_length=200, blank=True)  # 👈 Spécifique Odoo
    ai_techniques = models.CharField(_("Techniques IA"), max_length=200, blank=True)  # 👈 Spécifique IA
    
    github_url = models.URLField(_("Lien GitHub"), blank=True)
    live_url = models.URLField(_("Lien vers le projet"), blank=True)
    
    # Visuels
    image = models.ImageField(_("Image principale"), upload_to='projects/', blank=True)
    display_order = models.IntegerField(_("Ordre d'affichage"), default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['display_order', '-created_at']
        verbose_name = _("Projet")
        verbose_name_plural = _("Projets")
    
    def __str__(self):
        return self.title

class Experience(models.Model):
    EXPERIENCE_TYPES = [
        ('WORK', 'Expérience professionnelle'),
        ('RESEARCH', 'Recherche'),
        ('ACADEMIC', 'Académique'),
        ('VOLUNTEER', 'Bénévolat'),
    ]
    
    title = models.CharField(_("Poste"), max_length=200)
    company = models.CharField(_("Entreprise/Organisation"), max_length=200)
    experience_type = models.CharField(_("Type d'expérience"), max_length=10, choices=EXPERIENCE_TYPES)
    
    start_date = models.DateField(_("Date de début"))
    end_date = models.DateField(_("Date de fin"), null=True, blank=True)  # Null = toujours en poste
    current = models.BooleanField(_("Actuel"), default=False)
    
    description = models.TextField(_("Description"))
    technologies = models.CharField(_("Technologies utilisées"), max_length=300, blank=True)
    
    display_order = models.IntegerField(_("Ordre d'affichage"), default=0)
    
    class Meta:
        ordering = ['-start_date', 'display_order']
        verbose_name = _("Expérience")
        verbose_name_plural = _("Expériences")
    
    def __str__(self):
        return f"{self.title} chez {self.company}"

class Publication(models.Model):
    title = models.CharField(_("Titre"), max_length=300)
    authors = models.CharField(_("Auteurs"), max_length=400)
    conference = models.CharField(_("Conférence/Journal"), max_length=200)
    year = models.IntegerField(_("Année"))
    
    paper_url = models.URLField(_("Lien vers le papier"), blank=True)
    code_url = models.URLField(_("Lien vers le code"), blank=True)
    
    abstract = models.TextField(_("Résumé"), blank=True)
    
    class Meta:
        ordering = ['-year']
        verbose_name = _("Publication")
        verbose_name_plural = _("Publications")
    
    def __str__(self):
        return self.title

class SkillCategory(models.Model):
    name = models.CharField(_("Nom de la catégorie"), max_length=100)
    display_order = models.IntegerField(_("Ordre d'affichage"), default=0)
    
    class Meta:
        ordering = ['display_order']
        verbose_name = _("Catégorie de compétence")
        verbose_name_plural = _("Catégories de compétences")
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    SKILL_LEVELS = [
        ('BEGINNER', 'Débutant'),
        ('INTERMEDIATE', 'Intermédiaire'), 
        ('ADVANCED', 'Avancé'),
        ('EXPERT', 'Expert'),
    ]
    
    name = models.CharField(_("Nom"), max_length=100)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    level = models.CharField(_("Niveau"), max_length=15, choices=SKILL_LEVELS)
    years_of_experience = models.DecimalField(_("Années d'expérience"), max_digits=3, decimal_places=1)
    
    class Meta:
        ordering = ['category__display_order', 'name']
        verbose_name = _("Compétence")
        verbose_name_plural = _("Compétences")
    
    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"

# Pilier 5 : Lead Engine
class ContactRequest(models.Model):
    name = models.CharField(_("Nom"), max_length=100)
    email = models.EmailField(_("Email"))
    company = models.CharField(_("Entreprise"), max_length=100, blank=True)
    subject = models.CharField(_("Sujet"), max_length=200, default="Demande de contact")
    message = models.TextField(_("Message"))
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(_("Traité"), default=False)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = _("Demande de contact")
        verbose_name_plural = _("Demandes de contact")
    
    def __str__(self):
        return f"Contact de {self.name} - {self.created_at.strftime('%d/%m/%Y')}"