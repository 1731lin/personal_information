from django.db import models

# Create your models here.
class Blog(models.Model):

	title = models.CharField(default='文章', max_length=50)
	date = models.DateField()
	image = models.ImageField(default='default.png',upload_to='imges/')
	text = models.TextField(default='文章正文')
	def __str__(self) :
		 return self.title


   	
   	
    