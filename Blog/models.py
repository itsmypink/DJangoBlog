from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category (models.Model):
	name = models.CharField(max_length=100)
	
	
class Tag(models.Model):
	name=models.CharField(max_length=100)
	
class Post(models.Model):
	title = models.CharField(max_length=100)
	body=models.TextField()
	created_time=models.DateTimeField()
	modfied_time=models.DateTimeField()
	excerpt=models.CharField(max_length=200,blank=True)
	category=models.ForeignKey(Category)
	tags=models.ManyToManyField(Tag,blank=True)
	author=models.ForeignKey(User)
	views = models.PositiveIntegerField(default=0,blank=True)
	
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('Blog:detail', kwargs={'pk': self.pk})
	def increase_views(self):
		self.views+= 1
		self.save(update_fields=['views'])
	class Meta:
		ordering=["-created_time"]