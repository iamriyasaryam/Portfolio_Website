from django.contrib import admin
from . models import SkillCategory, SkillModel, HighlightModel, ProjectModel, ExperienceModel, AchievementModel, ResumeModel

# Register your models here.

#==============SKILL================#

class SkillInline(admin.TabularInline):
    model = SkillModel
    extra = 1

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    inlines = [SkillInline]
    list_display = ("name", "meta")

@admin.register(SkillModel)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "percentage")

@admin.register(HighlightModel)
class HighlightAdmin(admin.ModelAdmin):
    list_display = ("text",)
    

@admin.register(ProjectModel)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title"]

@admin.register(ExperienceModel)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "role", "start_date", "end_date", "is_current")

@admin.register(AchievementModel)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "link")

@admin.register(ResumeModel)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("id", "updated_at")