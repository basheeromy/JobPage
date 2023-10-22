from datetime import *
from django.db import models

from django.contrib.auth.models import User
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point

from django.core.validators import(
                MinValueValidator,
                MaxValueValidator
)
import geocoder
import os


class JobType(models.TextChoices):
    """
    JobType options.
    """
    Permanent = 'Permanent'
    Temporary = 'Temporary'
    Internship = 'Internship'


class Education(models.TextChoices):
    """
    Education options.
    """
    Bachelors = 'Bachelors'
    Masters = 'Masters'
    Phd = 'Phd'


class Industry(models.TextChoices):
    """
    Industry options.
    """
    Business = 'Business'
    IT = 'Information Technology'
    Banking = 'Banking'
    Telecommunication = 'Telecommunication'
    Others = 'Others'


class Experience(models.TextChoices):
    """
    JobType options.
    """
    NO_EXPERIENCE = 'No Experience'
    ONE_YEAR = '1 Year'
    TWO_YEAR = '2 Years'
    TREE_YEAR_PLUS = '3 Years above'


def return_date_time():
    """
    Function which returns current date and time.
    """
    now = datetime.now()
    return now + timedelta(days=10)


class Job(models.Model):
    """
    Database model to store data of jobs to be posted.
    """
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=100, null=True)
    jobType = models.CharField(
        max_length=10,
        choices=JobType.choices,
        default=JobType.Permanent
    )
    education = models.CharField(
        max_length=10,
        choices=Education.choices,
        default=Education.Bachelors
    )
    industry = models.CharField(
        max_length=30,
        choices=Industry.choices,
        default=Industry.Business
    )
    experience = models.CharField(
        max_length=20,
        choices=Experience.choices,
        default=Experience.NO_EXPERIENCE
    )
    salary = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100000000)
        ]
    )
    positions = models.IntegerField(default=1)
    company = models.CharField(max_length=100, null=True)
    point = gismodels.PointField(default=Point(0.0, 0.0))
    lastDate = models.DateTimeField(default=return_date_time)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    createdAt = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Over ride the save method.

        g = geocoder.mapquest(
            self.address,
            key=os.environ.get('GEOCODER_API')
        )

        print(g)

        lng = g.lng
        lat = g.lat

        self.point = Point(lng, lat)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
