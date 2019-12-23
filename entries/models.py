from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Entry(models.Model):
    entry_title = models.CharField(max_length=50)
    entry_text = models.TextField()
    entry_date = models.DateTimeField(auto_now_add=True)
    entry_author = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return f'{self.entry_title}'

class Profile(models.Model):
    Full_Name = models.CharField(max_length=50)
    Bio = models.TextField()
    Registration_date = models.DateTimeField(auto_now_add=True)
    Facebook_link = models.CharField(max_length=100)
    Instagram_link = models.CharField(max_length=100)
    Twitter_link = models.CharField(max_length=100)
    Profile_image = models.ImageField(upload_to='pictures/%Y/%m/%d/', max_length=255,  blank=True)
    User = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Profile')

    class Meta:
        verbose_name_plural = "profiles"
    
    def __str__(self):
        return f'{self.User.username}'
    