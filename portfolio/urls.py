from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('achievements/', views.achievements, name='achievements'),
    path("resume/view/", views.resume_view, name="resume_view"),
    path("resume/download/", views.resume_download, name="resume_download"),
    path('sendmail/', views.sendmail, name='sendmail'),
]
