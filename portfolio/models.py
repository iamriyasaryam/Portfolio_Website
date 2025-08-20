from django.db import models

# Create your models here.
#|| =============  SKILL ===================||

#category like language, frontend, backend, ai/ml and highlights
class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    meta = models.CharField(max_length=200, blank=True, null=True)  # Core, ui/ux stack

    def __str__(self):
        return self.name
    
#Each individual skill inside a category
class SkillModel(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=100) # java, python
    percentage = models.PositiveIntegerField(default=0) # e.g 80
    tags = models.CharField(max_length=255, blank=True, null=True)  # comma saperted tags like oops, rest

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"

   
# NEW MODEL for Highlights section 
class HighlightModel(models.Model):
    text = models.CharField(max_length=100)  # e.g., "Problem Solving"

    def __str__(self):
        return self.text


# Project Model
class ProjectModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField()
    repo = models.URLField()

    def __str__(self):
        return self.title


class ExperienceModel(models.Model):
    title = models.CharField(max_length=200)   # e.g. "Senior Developer"
    role = models.CharField(max_length=200) # e.g. "Tech Solutions Inc."
    logo = models.ImageField(upload_to='experience_logos/')  
    start_date = models.DateField()  
    end_date = models.DateField(blank=True, null=True)  # null if still working
    is_current = models.BooleanField(default=False)  # to mark ongoing job
    description = models.TextField()  # role details and responsibilities

    class Meta:
        ordering = ['-start_date']  # latest job first

    def __str__(self):
        return f"{self.title} at {self.role}"
    
    
# Achievements Model
class AchievementModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='achievements/')
    link = models.URLField()

    def __str__(self):
        return self.title


#Resume 
class ResumeModel(models.Model):
    name = models.CharField(max_length=100, default="Riya Saryam")
    file = models.FileField(upload_to='resumes/', blank=True, null=True)  # Optional field for resume file
    external_link = models.URLField(blank=True, null=True)  # Optional field for external resume link
    updated_at = models.DateTimeField(auto_now=True)  # Auto-update field for tracking changes

    def __str__(self):
        return self.name