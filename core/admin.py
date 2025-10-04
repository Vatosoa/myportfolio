from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Project, Experience, Publication, SkillCategory, Skill, ContactRequest, AboutContent, CVFile

class AboutContentAdmin(admin.ModelAdmin):
    list_display = ['language', 'updated_at']
    list_display_links = ['language']  # On clique sur la langue pour éditer
    
    def has_add_permission(self, request):
        return AboutContent.objects.count() < 2
               
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'project_type', 'display_order', 'created_at', 'updated_at']
    list_filter = ['project_type', 'created_at']
    search_fields = ['title', 'challenge', 'technologies']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (_('Informations générales'), {
            'fields': ('title', 'slug', 'project_type', 'display_order')
        }),
        (_('Récit du projet - Pilier 3'), {
            'fields': ('challenge', 'solution', 'result')
        }),
        (_('Technologies et liens'), {
            'fields': ('technologies', 'odoo_modules', 'ai_techniques', 'github_url', 'live_url')
        }),
        (_('Visuel'), {
            'fields': ('image',)
        }),
    )

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'experience_type', 'start_date', 'end_date', 'current', 'display_order']
    list_filter = ['experience_type', 'current', 'start_date']
    search_fields = ['title', 'company', 'description']
    fieldsets = (
        (_('Informations générales'), {
            'fields': ('title', 'company', 'experience_type', 'display_order')
        }),
        (_('Dates'), {
            'fields': ('start_date', 'end_date', 'current')
        }),
        (_('Description'), {
            'fields': ('description', 'technologies')
        }),
    )

class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'conference', 'year']
    list_filter = ['year', 'conference']
    search_fields = ['title', 'authors', 'conference']
    fieldsets = (
        (_('Informations de publication'), {
            'fields': ('title', 'authors', 'conference', 'year')
        }),
        (_('Liens et contenu'), {
            'fields': ('paper_url', 'code_url', 'abstract')
        }),
    )

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_order']
    list_editable = ['display_order']
    inlines = [SkillInline]

class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'level', 'years_of_experience']
    list_filter = ['category', 'level']
    search_fields = ['name']

class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'company', 'subject', 'created_at', 'is_processed']
    list_filter = ['is_processed', 'created_at']
    search_fields = ['name', 'email', 'company', 'message']
    readonly_fields = ['name', 'email', 'company', 'subject', 'message', 'created_at']
    
    def has_add_permission(self, request):
        return False  # Empêcher la création manuelle de demandes de contact


from .models import CVFile  # 👈 Ajoutez cet import

class CVFileAdmin(admin.ModelAdmin):
    list_display = ['language', 'title', 'is_active', 'updated_at']
    list_editable = ['is_active']
    list_display_links = ['language']
    
    def has_add_permission(self, request):
        return CVFile.objects.count() < 2

# Enregistrement des modèles dans l'admin
admin.site.register(Project, ProjectAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(SkillCategory, SkillCategoryAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(ContactRequest, ContactRequestAdmin)
admin.site.register(AboutContent, AboutContentAdmin)
admin.site.register(CVFile, CVFileAdmin)

# Personnalisation du titre de l'admin
admin.site.site_header = _("Administration du Portfolio de Vatosoa")
admin.site.site_title = _("Portfolio Admin")
admin.site.index_title = _("Gestion du contenu du portfolio")