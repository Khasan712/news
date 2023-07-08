from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomManager

class User(AbstractBaseUser, PermissionsMixin):
    ROLE = (
        ('admin', 'admin'),
        ('user', 'user'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50)
    avatar = models. ImageField(upload_to='user/avatar/', blank=True, null=True)
    role = models.CharField(max_length=5, choices=ROLE, default=ROLE[1][0])
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", 'role']

    def __str__(self) -> str:
        return f'{self.email} {self.first_name}'