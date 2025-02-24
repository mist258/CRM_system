from django.contrib.auth.models import UserManager as Manager


class UserCustomManager(Manager):

    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Email address required')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_unusable_password()
        user.save()
        return user

    def create_manager(self, email=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)

        return self.create_user(email=email, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be staff')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be superuser')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must be active')

        user = self.create_user(email, password, **extra_fields)
        user.set_password(password)
        user.save()
        return user
