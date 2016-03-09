from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django_summernote import models as summer_models
from django_summernote import fields as summer_fields

CONDITION_OF_ITEM = (
    ('S', '아직 미개봉'),
    ('A', '거의 새것'),
    ('B', '사용감 있음'),
    ('C', '오래됨'),
)

WAY_OF_DEAL = (
    ('direct', '직거래'),
    ('ship', '택배'),
)

STATE_OF_ITEM = {
    ('sold', '판매완료'),
    ('sale', '판매중'),
}

class Category(models.Model):
    name = models.CharField('카테고리 이름', max_length=100)

    def __str__(self):
        return self.name


class ItemManager(models.Manager):
    pass

class Item(models.Model):

    vendor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='판매자')
    category = models.ForeignKey(Category, verbose_name='카테고리')
    created_at = models.DateTimeField('등록일', auto_now_add=True)
    updated_at = models.DateTimeField('수정일', auto_now=True)
    name = models.CharField('이름', max_length=200)
    deal_place = models.CharField('거래장소', max_length=10, null=True, blank=True)
    include_shipping = models.BooleanField('배송료포함', default=False, blank=True)
    deal_way = models.CharField('거래방법', max_length=6, choices=WAY_OF_DEAL, default='direct', null=False, blank=False)
    condition = models.CharField('물품상태', max_length=1, choices=CONDITION_OF_ITEM, default='B', null=False, blank=False)
    desc = models.TextField('설명', null = False, max_length=1000)
    price = models.CommaSeparatedIntegerField('판매가', max_length=10, default=10000)
    # shipping_price = models.CommaSeparatedIntegerField('배송료', max_length=10, null=True, blank=True)
    state = models.CharField('판매여부', max_length=4, choices=STATE_OF_ITEM, default='sale', null=False, blank=False)

    objects = ItemManager()


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('shop:item_detail', kwargs={'item_id':self.id})

class ItemPhoto(models.Model):
    item = models.ForeignKey(Item, related_name='photos_of_item')
    image = models.ImageField(upload_to='%Y%m%d')

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(ItemPhoto, self).delete(*args, **kwargs)

class ItemComment(models.Model):
    body = models.CharField('코멘트', max_length=300)
    created_at = models.DateTimeField('등록일', auto_now_add=True)
    updated_at = models.DateTimeField('수정일', auto_now=True)
    item = models.ForeignKey(Item, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments')


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

    nickname = models.CharField('별명', max_length=20, unique=True)

    STATES_OF_CREDIBILITY = (
        ('vendor', '거상'),
        ('pro', '프로'),
        ('newbie', '뉴비'),
    )

    credibility = models.CharField(max_length=10,
                                   choices=STATES_OF_CREDIBILITY,
                                   default='newbie')

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

    def get_nickname(self):
        return self.nickname

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