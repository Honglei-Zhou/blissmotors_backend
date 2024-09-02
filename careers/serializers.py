from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import JobApplicant, Job


class JobSerializer(serializers.ModelSerializer):

    job_id = serializers.CharField(required=True,
                                   validators=[UniqueValidator(queryset=Job.objects.all())])
    job_title = serializers.CharField(required=True)
    responsibilities = serializers.CharField(required=True)
    qualifications = serializers.CharField(required=True)
    contact = serializers.CharField(required=True)

    expiration_date = serializers.DateField(required=True)

    def create(self, validated_data):

        job_id = validated_data.get('job_id')
        job_title = validated_data.get('job_title')

        responsibilities = validated_data.get('responsibilities')
        qualifications = validated_data.get('qualifications')

        contact = validated_data.get('contact')

        expiration_date = validated_data.get('expiration_date')

        job = Job(job_id=job_id, job_title=job_title, responsibilities=responsibilities,
                  qualifications=qualifications, contact=contact, expiration_date=expiration_date)

        job.save()
        return job

    class Meta:
        model = Job
        fields = ('job_id', 'job_title', 'responsibilities',
                  'qualifications', 'contact', 'expiration_date')


class JobListSerializer(serializers.ModelSerializer):
    job_id = serializers.CharField(required=True)
    job_title = serializers.CharField(required=True)
    expiration_date = serializers.DateField(required=True)

    class Meta:
        model = Job
        fields = ('id', 'job_id', 'job_title', 'expiration_date')


class JobApplicantSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    email = serializers.EmailField(required=True)
    phone = serializers.CharField(required=True)

    job_id = serializers.CharField(required=True)
    job_title = serializers.CharField(required=True)

    working_time = serializers.CharField(required=True)
    why_bm = serializers.CharField(required=False, default='')
    skills_experience = serializers.CharField(required=False, default='')
    resume = serializers.CharField(required=True)

    def create(self, validated_data):
        email = validated_data.get('email')
        phone = validated_data.get('phone')

        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')

        job_id = validated_data.get('job_id')
        job_title = validated_data.get('job_title')

        working_time = validated_data.get('working_time')
        why_bm = validated_data.get('why_bm')

        skills_experience = validated_data.get('skills_experience')

        resume = validated_data.get('resume')

        job_applicant = JobApplicant(first_name=first_name, last_name=last_name,
                                     email=email, phone=phone, job_id=job_id, job_title=job_title,
                                     working_time=working_time, resume=resume)

        if why_bm:
            job_applicant.why_bm = why_bm
        if skills_experience:
            job_applicant.skills_experience = skills_experience

        job_applicant.save()
        return job_applicant

    class Meta:
        model = Job
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'job_id',
                  'job_title', 'working_time', 'why_bm', 'skills_experience', 'resume')


class JobApplicantListSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    email = serializers.EmailField(required=True)
    phone = serializers.CharField(required=True)

    job_id = serializers.CharField(required=True)
    job_title = serializers.CharField(required=True)

    class Meta:
        model = Job
        fields = ('id', 'job_id', 'job_title', 'first_name', 'last_name')
        ordering = ['job_id']
