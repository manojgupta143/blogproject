from django.db import models
from django.contrib.auth .models import User 
from django.urls import reverse
from django.utils import timezone    
# Create your models here.
from taggit.managers import TaggableManager
class CustomManager(models.Manager):
    def get_queryset(self) :
        return super().get_queryset().filter(status='published').order_by('-publish')
class Post(models.Model):
    CHOICES_STATUS=(('draft','Draft'),('published','Published'))
    title=models.CharField( max_length=100)
    slug=models.SlugField(max_length=100,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_post', on_delete=models.CASCADE)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=False)
    status=models.CharField( max_length=50,choices=CHOICES_STATUS, default='Draft')
    objects=CustomManager()
    tags=TaggableManager()


    class Meta:
        ordering=('-publish',) 
    def __str__(self):
        return self.title
    def get_absolute_url(self): 
       return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])  
class Comment(models.Model):
    post=models.ForeignKey(Post, related_name=('comments'), on_delete=models.CASCADE)
    name=models.CharField( max_length=32)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField( auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    class Meta:
        ordering=('-created',)
    def __str__(self):
        return 'Cammnted by{} on {}'.format(self.name,self.post)

 

