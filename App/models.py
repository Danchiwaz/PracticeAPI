from django.db import models
from PIL import Image

class Person(models.Model):
	firstName = models.CharField(max_length = 100, null = True)
	lastName  = models.CharField(max_length = 100, null = True)
	email     = models.EmailField()
	image     = models.ImageField(upload_to ="Api_pics" ,null = True, blank=True)

	class Meta:
		verbose_name = "Person"
		verbose_name_plural = "Persons"

	def __str__(self):
		return self.firstName

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		img = Image.open(self.image.path)

		if img.height >300 or img.width >300:
			img_size = (300, 300)
			img.thumbnail(img_size)
			img.save(self.image.path)
		
		
