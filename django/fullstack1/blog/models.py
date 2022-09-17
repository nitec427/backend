from django.db import models
from django.conf import settings
# Create your models here.
# each of the models will inherit from models.Model class


# Profile model

class Profile(models.Model):
    # User is a 1-to-1 associatation to the Django user with which the profile is associated
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)
    
    def __str__(self):
        return self.user.get_username()
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    
    class Meta:
        # show the most recently published posts first
        ordering = ["-publish_date"]
        
    title = models.CharField(max_length=50, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    body = models.TextField()
    meta_description = models.CharField(max_length=255, blank=True)
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    
    # The line below (models.PROTECT) ensures that you can't delete an author with posts.
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    
    
    tags = models.ManyToManyField(Tag, blank=True)
    