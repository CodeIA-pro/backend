from djongo import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        if not email: # If email is not provided 
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields) # Normalize email
        user.set_password(password) # Set password
        user.save(using=self._db) # Save user
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password)
        user.role = 'admin'
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db) # ._db meaning the database that is being used
        return user

class TypeComment(models.Model):
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Star(models.Model):
    value = models.IntegerField(primary_key=True, blank=False)
    class Meta:
        managed = False

class Comment(models.Model):
    user = models.IntegerField(blank=False)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    type_comment = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Subscription(models.Model):
    id_plan = models.IntegerField(blank=False)
    user_id = models.IntegerField(blank=False)
    months_duration = models.IntegerField(blank=False)
    activation_code = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)
    is_activated = models.BooleanField(default=False, blank=True)
    due_date = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class FAQ(models.Model):
    question = models.CharField(max_length=100, blank=True)
    answer = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Forgotten(models.Model):
    link = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Asset(models.Model):
    version = models.CharField(max_length=10, default='1.0.0', blank=True)
    is_Loading = models.BooleanField(default=False, blank=True)
    titulo = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    more_description = models.TextField(blank=True)
    depth = models.IntegerField(default=0, blank=True)
    lang = models.CharField(max_length=100, blank=True)
    url_commit = models.TextField(blank=True, default='')
    short_sha = models.CharField(max_length=100, blank=True, default='')
    url = models.TextField(blank=True)
    privacy = models.CharField(max_length=100, blank=True, default='private')
    to_failed = models.BooleanField(default=False, blank=True)
    message_failed = models.TextField(blank=True, default='')
    theme = models.CharField(max_length=100, blank=True, default='')
    is_father = models.BooleanField(default=False, blank=True)
    father_id = models.IntegerField(blank=False)
    project_id = models.IntegerField(blank=True)
    subsection = models.ArrayReferenceField(to='self', default=list, blank=True)
    stars = models.ArrayField(model_container=Star, null=True, default=list)


class Project(models.Model):
    title = models.CharField(max_length=100, blank=True)
    branch = models.CharField(max_length=100, blank=True)
    url_repo = models.TextField(blank=True)
    user_repo = models.TextField(blank=True)
    last_short_sha = models.CharField(max_length=100, blank=True)
    root = models.CharField(max_length=100, blank=True)
    latest_build = models.DateTimeField(default='', blank=True)
    is_Loading = models.BooleanField(default=False, blank=True)
    status = models.CharField(max_length=100, blank=True)
    last_version = models.CharField(max_length=100, blank=True)
    template = models.TextField(blank=True, default='default')
    message_failed = models.TextField(blank=True, default='')
    guide_running = models.BooleanField(default=False, blank=True)
    lang = models.CharField(max_length=100, blank=True)
    information = models.TextField(blank=True)
    url_info = models.TextField(blank=True)
    serializer_info = models.TextField(blank=True)
    view_info = models.TextField(blank=True)
    urls = models.TextField(blank=True, default='')
    assets = models.ArrayReferenceField(to=Asset, default=list, blank=True)

class Repository(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    projects = models.ArrayReferenceField(to=Project, default=list, blank=True)

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    is_unverified = models.BooleanField(default=True)
    date_of_birth = models.DateField(null=True)
    token_repo = models.TextField(blank=True)
    repo_login = models.BooleanField(default=False)
    user_github = models.CharField(max_length=100, blank=True)
    projects = models.ArrayReferenceField(to=Project, default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    verification_code = models.IntegerField(default=0, blank=True)
    is_active = models.BooleanField(default=True)
    two_factor = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    plan = models.IntegerField(default=0)
    role = models.CharField(max_length=20, default='guest')
    objects = UserManager()

    USERNAME_FIELD = 'email' # This is the field that will be used to login