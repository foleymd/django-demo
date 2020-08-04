from django.db import models
from emdash.constants import MONTH_CHOICES, YEAR_CHOICES
# from users.models import CustomUser
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.

class PersonStart(models.Model):
    """Initial values for person"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
    investments_start = models.DecimalField(max_digits=8, decimal_places=2, help_text='The amount you have invested up to now.', default=0)
    savings_start = models.DecimalField(max_digits=8, decimal_places=2, help_text='The amount you have saved up to now.', default=0)

    def __str__(self):
        return self.user.email

    def get_absolute_url(self):
        return reverse('person-start-detail-view', args=[str(self.id)])

class PersonMonth(models.Model):
    """Monthly summary of financial habits"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
    year = models.CharField(max_length=4, choices=YEAR_CHOICES, default='2020')
    month =  models.CharField(max_length=2, choices=MONTH_CHOICES, default='01')
    income = models.DecimalField(max_digits=8, decimal_places=2, help_text='Your total income this month.', default=0)
    savings = models.DecimalField(max_digits=8, decimal_places=2, help_text='The amount you saved this month.', default=0)
    investments = models.DecimalField(max_digits=8, decimal_places=2, help_text='The amount you invested this month.', default=0)
    spent = models.DecimalField(max_digits=8, decimal_places=2, help_text='The amount you spent this month.', default=0)

    def __str__(self):
        return self.year + '-' + self.month

    def verbose_month(self):
        return month.label

    def get_absolute_url(self):
        return reverse('person-month-detail-view', args=[str(self.id)])
