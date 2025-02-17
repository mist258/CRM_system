from django.db import models

from core.models import BaseModel

from .choices.application_choices import CoursesChoices, FormatCourseChoices, StatusChoices, TypeCourseChoices


class StudentApplicationModel(BaseModel):
    class Meta:
        db_table = 'student_application'
        ordering = ('id',)

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    age = models.IntegerField()
    course = models.CharField(max_length=4, choices=CoursesChoices.choices,
                              blank=True, null=True)
    course_format = models.CharField(max_length=6, choices=FormatCourseChoices.choices,
                                     blank=True, null=True)
    course_type = models.CharField(max_length=9, choices=TypeCourseChoices.choices,
                                   blank=True, null=True)
    status = models.CharField(max_length=8, choices=StatusChoices.choices,
                               blank=True, null=True)
    sum = models.DecimalField(max_digits=5, decimal_places=0,
                              blank=True, null=True)
    alreadyPaid = models.DecimalField(max_digits=5, decimal_places=0,
                                      blank=True, null=True)
    group = ...
    manager = ...




