from django.db import models
import slugify

# Create your models here.

JOB_NATURE = (
    ('Full-Time','Full-Time'),
    ('Part-Time','Part-Time'),
)

class Job(models.Model):
    # # FKs
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    # slug
    slug = models.SlugField(blank=True, null=True)

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
    
    def save(self, *args, **kwargs):
        self.slug = slugify.slugify(self.title)
        super(Job, self).save(*args, **kwargs)
    

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class Apply(models.Model):
    job = models.ForeignKey("Job", related_name="apply_job", on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=70)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



