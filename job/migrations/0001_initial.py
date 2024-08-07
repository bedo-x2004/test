# Generated by Django 5.0.7 on 2024-08-05 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=30)),
                ('job_nature', models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time')], max_length=15)),
                ('description', models.TextField(max_length=300)),
                ('published_on', models.DateTimeField(auto_now=True)),
                ('vacancy', models.IntegerField(default=1)),
                ('salary', models.IntegerField(default=0)),
            ],
        ),
    ]
