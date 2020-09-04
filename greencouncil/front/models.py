from django.db import models
from django.conf import settings


# Create your models here.
from django.dispatch import Signal


class Learner(models.Model):
    learner_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=66, help_text="current job description")
    linkedin_url = models.URLField(max_length=200, help_text="your Linked profile link")
    

  
