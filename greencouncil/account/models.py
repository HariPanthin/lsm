from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.

class Learner(models.Model):
    learner_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=66, help_text="current job desription")
    linkedin_url = models.URLField(max_length=200, help_text="your linked profile link")
    country = CountryField(blank_label='(select country)')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'learner' 
        verbose_name_plural = 'learners'