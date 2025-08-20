from django.shortcuts import render, redirect
from .models import SkillCategory, HighlightModel, ProjectModel, ExperienceModel, AchievementModel, ResumeModel
from django.core.mail import send_mail
from .forms import EmailForm
from django.conf import settings
from django.http import FileResponse, Http404
from pathlib import Path


#===========SKILL VIEW==============#
def home(request):
    categories = SkillCategory.objects.prefetch_related("skills").all()
    highlights = HighlightModel.objects.all()
    projects = ProjectModel.objects.all()[:3]
    experiences = ExperienceModel.objects.all()
    for category in categories:
        for skill in category.skills.all():   # loop over related skills
             if skill.tags:  # only split if not None/empty
                skill.tag_list = skill.tags.split(",")
             else:
                skill.tag_list = []  # no tags
    return render(request, 'portfolio/index.html', {"categories": categories, "highlights": highlights, 'projects': projects, 'experiences': experiences})


def sendmail(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            ms = form.save()
            # Send email
            send_mail(
               subject = "Alert You Got message from your portfolio",
               message = f"From:{ms.email}\n\n{ms.message}",
               from_email = settings.EMAIL_HOST_USER,
               recipient_list=['iamriyasaryam@gmail.com'],
               fail_silently=False,
            )
        return render(request, 'portfolio/index.html', {'form': form})
    else:
        form = EmailForm()
    return render(request, 'portfolio/index.html', {'form':form})



def projects(request):
    projects = ProjectModel.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})


def achievements(request):
    achievements = AchievementModel.objects.all()
    return render(request, 'portfolio/certificates.html', {'achievements': achievements})



def _get_latest_resume():
    return ResumeModel.objects.order_by("-updated_at").first()

def resume_view(request):
    """Open PDF in browser (new tab)"""
    resume = _get_latest_resume()
    if not resume:
        raise Http404("Resume not found")

    # If you prefer using an external link (Drive), just redirect:
    if resume.external_link and not resume.file:
        return redirect(resume.external_link)

    if not resume.file:
        raise Http404("Resume file not uploaded")

    return FileResponse(
        resume.file.open("rb"),
        content_type="application/pdf",  # lets browsers render inline
        as_attachment=False
    )

def resume_download(request):
    """Force download of PDF"""
    resume = _get_latest_resume()
    if not resume or not resume.file:
        raise Http404("Resume file not found")

    filename = Path(resume.file.name).name
    return FileResponse(
        resume.file.open("rb"),
        as_attachment=True,
        filename=filename  # sets Content-Disposition: attachment; filename="..."
    )