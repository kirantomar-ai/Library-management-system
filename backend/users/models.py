from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin


class UserAccountManager(BaseUserManager):
    def create_user(self, name, phone,address , college, email, password=None ):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email((email))
        email = email.lower()

        user = self.model(
            name=name,
            phone=phone,
            address=address,
            college=college,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, phone,address , college, email, password=None):
        user = self.create_user(
            name,
            phone,
            address,
            email,
            college,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
    
class UserAccount(AbstractBaseUser,PermissionsMixin):
    name= models.CharField(max_length=255)
    phone= models.CharField(max_length=255)
    address= models.CharField(max_length=255)
    college= models.CharField(max_length=255)
    email= models.EmailField(unique=True, max_length=255)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS=['name','phone','address','college']

    def __str__(self):
        return self.email

