from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('blog', views.BlogView)
router.register('comment', views.CommentView)
router.register('skill', views.SkillView)
router.register('experience', views.ExperienceView)
router.register('project', views.ProjectView)
router.register('project-image', views.ProjectImageView)
router.register('academic', views.AcademicView)





urlpatterns = [

    path('',  include(router.urls)),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)