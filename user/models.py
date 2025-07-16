from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.gis.db import models as gis_models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = gis_models.PointField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    hiking_experience = models.CharField(
        max_length=20,
        choices=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
            ('expert', 'Expert'),
        ],
        default='beginner'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    emergency_contact_name = models.CharField(max_length=100, blank=True)
    emergency_contact_phone = models.CharField(max_length=20, blank=True)
    preferred_difficulty = models.CharField(
        max_length=20,
        choices=[
            ('easy', 'Easy'),
            ('moderate', 'Moderate'),
            ('hard', 'Hard'),
            ('extreme', 'Extreme'),
        ],
        default='easy'
    )
    total_hikes_completed = models.IntegerField(default=0)
    total_distance_hiked = models.FloatField(default=0.0)  # in kilometers
    favorite_trails = models.ManyToManyField('trails.Trail', blank=True)
    
    def __str__(self):
        return f"{self.user.email} Profile"