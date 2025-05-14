from django.contrib.auth import get_user_model
from django.core import validators as v
from django.db import models

from apps.groups.models import GroupModel

from.choices.application_choices import CoursesChoices, FormatCourseChoices, StatusChoices, TypeCourseChoices
from core.models import BaseModel

from .regex import OrderValidationRegex

UserModel = get_user_model()


class OrdersModel(models.Model):

    class Meta:
        db_table = 'orders'
        ordering = ('-id',)

    name = models.CharField(max_length=25, validators=[v.RegexValidator(OrderValidationRegex.NAME_SURNAME.pattern,
                                                                                 OrderValidationRegex.NAME_SURNAME.msg)],
                                                                                 blank=True, null=True)
    surname = models.CharField(max_length=25, validators=[v.RegexValidator(OrderValidationRegex.NAME_SURNAME.pattern,
                                                                           OrderValidationRegex.NAME_SURNAME.msg)],
                                                                           blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, validators=[v.RegexValidator(OrderValidationRegex.PHONE_NUMBER.pattern,
                                                                         OrderValidationRegex.PHONE_NUMBER.msg)],
                                                                         blank=True, null=True)
    age = models.IntegerField(validators=[v.MinValueValidator(16), v.MaxValueValidator(100)],
                              error_messages={'Details':'Available year\'s range: 16 - 100'},
                              blank=True, null=True)
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
    created_at = models.DateTimeField(auto_now_add=True)
    manager = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, related_name='orders')
    group = models.ForeignKey(GroupModel, on_delete=models.SET_NULL, null=True, related_name='order_group')
