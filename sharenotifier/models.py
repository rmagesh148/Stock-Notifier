from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount

# Create your models here.


class StockDetails(models.Model):
    company_code = models.CharField(max_length=150, unique=True)
    target_price = models.FloatField(max_length=10)
    user = models.ForeignKey(User)

    class Meta:
        unique_together = (('company_code', 'user'),)
