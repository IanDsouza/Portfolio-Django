from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.timezone import now

class Blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    post = RichTextUploadingField()
    created = models.DateField(blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)
    rank = models.IntegerField(null=True, blank=True)
    like = models.IntegerField(null=True, blank=True)
    image = models.ImageField(
        upload_to="pictures/%Y%m/%d/", max_length=255, null=True, blank=True
    )

    @property
    def comments(self):
        return self.comment_set.all()

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey('blogs.Blog', on_delete=models.CASCADE )
    text = models.CharField(max_length=50)
    created = models.DateField(blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50,blank=True, null=True)  
    email =  models.CharField(max_length=50,blank=True, null=True)
    website = models.CharField(max_length=50,blank=True, null=True)

    def __str__(self):
        return self.text

class Skill(models.Model):
    name = models.CharField(max_length=50)
    exp = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=50)
    company =  models.CharField(max_length=50)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    discription = models.CharField(max_length=100)
    logo = models.ImageField(
        upload_to="logo/%Y%m/%d/", max_length=255, null=True, blank=True
    )
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=50)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    discription = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class  ProjectImage(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="project/%Y%m/%d/", max_length=255, null=True, blank=True
    )

    @property
    def images(self):
        return self.image_set.all()

    def __str__(self):
        return (str(self.project))


class Academic(models.Model):
    title = models.CharField(max_length=50)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    discription = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to="acad/%Y%m/%d/", max_length=255, null=True, blank=True
    )

    def __str__(self):
        return self.title






 

