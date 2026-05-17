from django.db import models


class WebUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class UserAddress(models.Model):
    user_address_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=20)


class AddressType(models.Model):
    address_type_id = models.AutoField(primary_key=True)
    home = models.CharField(max_length=50, null=True, blank=True)
    billing = models.CharField(max_length=50, null=True, blank=True)
    shipping = models.CharField(max_length=50, null=True, blank=True)


class UserPhone(models.Model):
    user_phone_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    phone_type_id = models.IntegerField()
    phone = models.CharField(max_length=50)


class PhoneType(models.Model):
    phone_type_id = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=50, null=True, blank=True)
    work = models.CharField(max_length=50, null=True, blank=True)
    home = models.CharField(max_length=50, null=True, blank=True)


class UserInfo(models.Model):
    user_info_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField()
    picture = models.TextField()


class PageData(models.Model):
    page_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    text = models.TextField()
    picture = models.TextField()
    landing_page = models.CharField(max_length=100)
    logged_pages = models.CharField(max_length=100)