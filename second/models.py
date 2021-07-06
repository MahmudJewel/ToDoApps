from django.db import models

# Create your models here.

class ItemList(models.Model):
	content = models.CharField(max_length=250)
	taking_date = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('taking_date',)
	def __str__(self):
		return self.content + '(' + str(self.id) + ')'


