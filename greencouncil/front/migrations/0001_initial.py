# Generated by Django 3.0.8 on 2020-08-14 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Learner',
            fields=[
                ('learner_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_title', models.CharField(help_text='current job description', max_length=66)),
                ('linkedin_url', models.URLField(help_text='your Linked profile link')),
            ],
        ),
    ]
