from django.db import models

# Create your models here.
class Events(models.Model):
	Title       = models.CharField(max_length =250)
	Coordinator = models.CharField(max_length =250, )
	Team        = models.IntegerField(null =False)

	def get_absulute_url(self):
		return f"/Events/{self.Coordinator}/"
