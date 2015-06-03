from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Member(AbstractUser):
    real_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u"{}, {}".format(self.username, self.real_name)


class Contact(models.Model):
    recipient = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    address = models.TextField()
    user = models.ForeignKey(Member, related_name='contact_member')

    def __unicode__(self):
        return u"{}".format(self.recipient, self.address)
# class Category(models.Model):
#     category = models.CharField(max_length=80)
#
#     def __unicode__(self):
#         return u"{}".format(self.category)

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

    def __unicode__(self):
        return u"{}".format(self.tag_name)


class Product(models.Model):
    cat_choice = (
        ('Toys', 'Toys'),
        ('Candies', 'Candies'),
        ('Lucky_draw', 'Lucky_draw')
    )
    category = models.CharField(max_length=20, choices=cat_choice)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, blank=True, null=True)
    have = models.BooleanField(default=True)
    price = models.PositiveSmallIntegerField(default=0)
    discount_S = models.BooleanField(default=False)
    discount_price = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    # cat = models.ForeignKey(Category, related_name='products')
    buyer = models.ManyToManyField(Member, related_name='prod_buyers', blank=True)
    tags = models.ManyToManyField(Tag, related_name="prod_tags", blank=True)
    photo = models.ImageField(
        upload_to='product_photos',
        blank=True,
        null=True,
        default='product_photos/default_img.jpg',
        help_text='use 480x480px jpg or bigger square photo'
    )
    publish_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return u"[{}] {}, {}".format(self.category, self.name, self.brand)


class Ads(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    activated = models.BooleanField(default=True)
    image = models.ImageField(
        upload_to='ad_photos',
        blank=True,
        null=True,
        default='ad_photos/default_img.jpg',
        help_text='use 2833px width x 1375px height jpg or photos in similar aspect ratio'
    )
    publish_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return u"{}".format(self.title)


class Buy_list(models.Model):
    buyer = models.ForeignKey(Member, related_name='buylist_member')

    create_date = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return u"{}: {}".format(self.buyer,)