from django.db import models

# Create your models here.
class Gallery(models.Model):
	description = models.CharField(default='在这里写作品简介', max_length=100)
	imge = models.ImageField(default='default.png',upload_to='imges/')   	
	title = models.CharField(default='作品标题', max_length=50)	  	
   	#在admin中显示标题
	def _str_(self):
		return self.title