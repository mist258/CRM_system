from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from core.models import BaseModel

from .choices.application_choices import CoursesChoices, FormatCourseChoices, StatusChoices, TypeCourseChoices

UserModel = get_user_model()


class GroupModel(models.Model):
    class Meta:
        db_table = 'group_order'
        ordering = ('id',)

    name = models.CharField(max_length=100, unique=True)

class OrdersModel(models.Model): # submain

    class Meta:
        db_table = 'orders'
        ordering = ('id',)

    name = models.CharField(max_length=25, validators=[validators.RegexValidator(regex=r'^[A-Za-z]*$')],
                            error_messages={'Details': 'Name is not valid'},
                            blank=True, null=True)
    surname = models.CharField(max_length=25, validators=[validators.RegexValidator(regex=r'^[A-Za-z]*$')],
                               error_messages={'Details': 'Surname is not valid'},
                               blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, validators=[validators.RegexValidator(regex=r'^\+?380\d{9}$')],
                             error_messages={'Details': 'Phone number is not valid'},
                             blank=True, null=True)
    age = models.IntegerField(validators=[validators.MinValueValidator(16), validators.MaxValueValidator(100)],
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
    group = models.OneToOneField(GroupModel, on_delete=models.SET_NULL, null=True, related_name='order_group')


class CommentsModel(BaseModel):
    class Meta:
        db_table = 'comments'
        ordering = ('id',)

    text = models.TextField(max_length=100)
    order = models.ForeignKey(OrdersModel, on_delete=models.SET_NULL, null=True, related_name='comments')
