from django.db import models
from django.utils import timezone

now = timezone.now()

class Group(models.Model):
	title   = models.CharField('Клуб атауы', max_length = 250)
	body    = models.TextField('Клуб жайында')
	picture = models.CharField('Клуб логотипі', max_length = 250, blank = True)
	users   = models.CharField('Клуб қолданушыларына', max_length = 3)

	def __str__(self):
		return self.title