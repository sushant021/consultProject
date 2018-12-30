from django.db import models
from django.urls import reverse


class BaseClass(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Country(BaseClass):
    pass

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class Institute(BaseClass):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='institutes')
    #location = models.TextField(blank=True)
    campuses = models.TextField(blank=True)
    is_university = models.BooleanField(default=True)

    class Meta:
        unique_together = (("name", "country"),)


class Discipline(BaseClass):
    pass


class Course(BaseClass):
    Bachelor = 'BCH'
    Diploma = 'DIP'
    PostGraduateDiploma = 'PGD'
    PostGraduateCertificate = 'PGC'
    Master = 'MST'
    Doctoral = 'DOC'

    level_choices = (
        (Bachelor, 'Bachelor'),
        (Diploma, 'Diploma'),
        (PostGraduateDiploma, 'Postgraduate Diploma'),
        (PostGraduateCertificate, 'Postgraduate Certificate'),
        (Master, 'Master'),
        (Doctoral, 'Doctoral'),
    )

    fee_level_choices = (
        ('First', '<$10,000'),
        ('Second', '$10,000 - $20,000'),
        ('Third', '$20,000 - $30,000'),
        ('Fourth', '$30,000 - $40,000'),
        ('Fifth', '>$40,000')

    )

    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='courses')
    discipline = models.ManyToManyField(Discipline, related_name='courses')
    duration = models.CharField(max_length=200, default='4 Years')
    level = models.CharField(max_length=3, choices=level_choices, default=Bachelor)
    fee = models.CharField(max_length=50, default='Unknown')
    fee_level = models.CharField(max_length=10, choices=fee_level_choices, default='Third')
    language_requirements = models.TextField(blank=True)
    academic_requirements = models.TextField(blank=True)
    description = models.TextField(blank=True)
    link_to_site = models.URLField(blank=True)
    intake_months = models.CharField(max_length=100,default='February/July')
    location = models.CharField(max_length=200, blank=True)

    class Meta:
        unique_together = (("slug", "institute"),)







