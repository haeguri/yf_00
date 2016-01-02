from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class Category(models.Model):
    name = models.CharField('카테고리 이름', max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, verbose_name='카테고리')
    name = models.CharField('이름', max_length=200)
    desc = models.TextField('설명', max_length=1000)
    created_at = models.DateTimeField('등록일', auto_now_add=True)
    updated_at = models.DateTimeField('수정일', auto_now=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.itemphoto_set.all().delete()
        super(Item, self).delete(*args, **kwargs)

class ItemPhoto(models.Model):
    item = models.ForeignKey(Item, related_name='photos_of_item')
    image = models.ImageField(upload_to='%Y%m%d')
    desc = models.TextField('사진설명', max_length=500)








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