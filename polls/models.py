from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models





class Deal(models.Model):
    key = models.AutoField(primary_key=True)
    deal_code = models.CharField(max_length=255)
    customer_code = models.IntegerField()
    service_code = models.CharField(max_length=255)
    promotion_code = models.CharField(max_length=255)
    pay_type = models.CharField(max_length=255)
    chnnel = models.CharField(max_length=255)
    charge_code = models.IntegerField()
    assistant = models.CharField(max_length=255, blank=True, null=True)
    complaint = models.CharField(max_length=255, blank=True, null=True)
    compliment = models.CharField(max_length=255, blank=True, null=True)
    delete_yn = models.CharField(max_length=255)
    etc_1 = models.CharField(max_length=255, blank=True, null=True)
    red_dt = models.DateTimeField(blank=True, null=True)
    eit_dt = models.DateTimeField(blank=True, null=True)
    reg_id = models.DateTimeField(blank=True, null=True)
    group_key = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deal'


class Promotion(models.Model):
    key = models.AutoField(primary_key=True)
    nm_kr = models.CharField(max_length=255, blank=True, null=True)
    nm_en = models.CharField(max_length=255, blank=True, null=True)
    r_p_a_choose = models.CharField(max_length=255, blank=True, null=True)
    ratio = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    use_yn = models.IntegerField()
    requester_id = models.IntegerField(blank=True, null=True)
    red_dt = models.DateTimeField(blank=True, null=True)
    eit_dt = models.DateTimeField(blank=True, null=True)
    reg_id = models.DateTimeField(blank=True, null=True)
    group_key = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promotion'


class Service(models.Model):
    key = models.AutoField(primary_key=True)
    nm_kr = models.CharField(max_length=255, blank=True, null=True)
    nm_en = models.CharField(max_length=255, blank=True, null=True)
    stock_code = models.IntegerField()
    price = models.BigIntegerField()
    use_yn = models.IntegerField()
    red_dt = models.DateTimeField(blank=True, null=True)
    eit_dt = models.DateTimeField(blank=True, null=True)
    reg_id = models.DateTimeField(blank=True, null=True)
    group_key = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service'


class StockComeR(models.Model):
    key = models.AutoField(primary_key=True)
    nm_kr = models.CharField(max_length=255, blank=True, null=True)
    nm_en = models.CharField(max_length=255, blank=True, null=True)
    ea = models.IntegerField()
    income_dt = models.DateTimeField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    up_key = models.IntegerField(blank=True, null=True)
    standard_bundle = models.IntegerField(blank=True, null=True)
    bundle = models.IntegerField(blank=True, null=True)
    red_dt = models.DateTimeField(blank=True, null=True)
    eit_dt = models.DateTimeField(blank=True, null=True)
    reg_id = models.CharField(max_length=255, blank=True, null=True)
    group_key = models.IntegerField(blank=True, null=True)
    use_yn = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_come_r'


class StockOutR(models.Model):
    key = models.AutoField(primary_key=True)
    nm_kr = models.CharField(max_length=255, blank=True, null=True)
    nm_en = models.CharField(max_length=255, blank=True, null=True)
    ea = models.IntegerField()
    out_dt = models.DateTimeField(blank=True, null=True)
    red_dt = models.DateTimeField(blank=True, null=True)
    eit_dt = models.DateTimeField(blank=True, null=True)
    reg_id = models.DateTimeField(blank=True, null=True)
    group_key = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_out_r'


class User(models.Model):
    key = models.AutoField(primary_key=True)
    level = models.IntegerField(blank=True, null=True)
    group = models.CharField(max_length=255, blank=True, null=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    nm_kr = models.CharField(max_length=255, blank=True, null=True)
    nm_en = models.CharField(max_length=255, blank=True, null=True)
    use_yn = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    red_dt = models.DateTimeField(blank=True, null=True)
    eit_dt = models.DateTimeField(blank=True, null=True)
    reg_id = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'