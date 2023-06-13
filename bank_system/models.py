# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    acc_no = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    acc_type = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    pin = models.CharField(max_length=255, blank=True, null=True)
    overdraft_limit = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    uncleared_balance = models.FloatField(blank=True, null=True)
    saving_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account'


class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user'
