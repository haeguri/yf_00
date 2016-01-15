from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django_summernote import models as summer_models
from django_summernote import fields as summer_fields

class Category(models.Model):
    name = models.CharField('카테고리 이름', max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    CONDITION_OF_ITEM = (
        ('S', 'S'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    )

    WAY_OF_DEAL = (
        ('direct', '직거래'),
        ('ship', '택배'),
        ('delivery', '직접배달')
    )

    vendor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='판매자')
    category = models.ForeignKey(Category, verbose_name='카테고리')
    name = models.CharField('이름', max_length=200)
    created_at = models.DateTimeField('등록일', auto_now_add=True)
    updated_at = models.DateTimeField('수정일', auto_now=True)
    price = models.CommaSeparatedIntegerField(max_length=10, default=10000)
    purchased_at = models.CharField('구입일', max_length=10)
    deal_way = models.CharField('거래방법', max_length=6,
                                choices=WAY_OF_DEAL,
                                default='direct')
    # desc = models.TextField(max_length=1000)
    condition = models.CharField('물품상태', max_length=1,
                                 choices=CONDITION_OF_ITEM,
                                 default='B')
    deal_place = models.CharField('거래장소', max_length=10,
                                  null=True, blank=True)
    shipping_price = models.CharField('배송료', max_length=10,
                                      null=True, blank=True)
    desc = models.TextField(null = False)
    # desc = summer_fields.SummernoteTextField()


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('shop:item_detail', kwargs={'item_id':self.id})

# class ItemDescription(summer_models.Attachment):
#     item = models.OneToOneField(Item, related_name='desc_of_item')
#     class_detail = summer_fields.SummernoteTextField()

class ItemPhoto(models.Model):
    item = models.ForeignKey(Item, related_name='photos_of_item')
    image = models.ImageField(upload_to='%Y%m%d')
    desc = models.TextField('사진설명', max_length=500)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(ItemPhoto, self).delete(*args, **kwargs)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='이메일',
        max_length=255,
        unique=True,
    )

    first_name = models.CharField('성', max_length=20)
    last_name = models.CharField('이름', max_length=20)

    LEVEL_OF_CREDIBILITY = (
        ('god', '신'),
        ('platinum', '플래티넘'),
        ('gold', '골드'),
        ('silver', '실버'),
        ('bronze', '브론즈'),
    )

    credibility = models.CharField(max_length=10,
                                   choices=LEVEL_OF_CREDIBILITY,
                                   default='bronze')

    joined_at = models.DateTimeField('가입일', auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin