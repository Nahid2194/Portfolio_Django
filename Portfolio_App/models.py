from django.db import models

# Create your models here.


class Skill(models.Model):
    skillname = models.CharField(max_length=30)
    skillPercent = models.IntegerField()

    def __str__(self):
        return self.skillname


class Project(models.Model):
    title = models.CharField(max_length=100)
    project_url = models.URLField(blank=True)
    project_pic = models.ImageField(upload_to='Project_pic', blank=True)

    def __str__(self):
        return self.title
