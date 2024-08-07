from django.db import models

# Create your models here.

JOB_NATURE = (
    ('Full-Time','Full-Time'),
    ('Part-Time','Part-Time'),
)

class Job(models.Model):
    # # FKs
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    # attributes
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=30)
    job_nature = models.CharField(max_length=15, choices=JOB_NATURE)
    description = models.TextField(max_length=300)
    published_on = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


