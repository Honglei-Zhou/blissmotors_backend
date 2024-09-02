from django.db import models


class JobApplicant(models.Model):
    id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)

    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=20, blank=False)

    job_id = models.CharField(max_length=10, blank=False)
    job_title = models.CharField(max_length=100, blank=False)
    working_time = models.CharField(max_length=30)
    why_bm = models.TextField()
    skills_experience = models.TextField()

    resume = models.TextField(blank=False)

    created = models.DateTimeField(auto_now_add=True)


class Job(models.Model):
    id = models.AutoField(primary_key=True)
    job_id = models.CharField(max_length=10, blank=False)
    job_title = models.CharField(max_length=100, blank=False)

    responsibilities = models.TextField()
    skills = models.TextField()

    experiences = models.TextField()
    requirements = models.TextField()

    contact = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    expiration_date = models.DateField(auto_now_add=True)

