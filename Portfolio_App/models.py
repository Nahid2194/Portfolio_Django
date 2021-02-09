from django.db import models

# Create your models here.


class Skill(models.Model):
    skillname = models.CharField(max_length=30)
    skillPercent = models.IntegerField()

    def __str__(self):
        return self.skillname
