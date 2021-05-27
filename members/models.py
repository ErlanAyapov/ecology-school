from django.db import models
from django.contrib.auth.models import User
from circle.models import Group

class Customer(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	birth_day    = models.CharField('туылға күні', max_length = 20)
	birth_mounth = models.CharField('туылға айы', max_length = 20)
	birth_year   = models.CharField('туылға жылы', max_length = 20)

	circle = models.ForeignKey(Group, on_delete = models.CASCADE)

	def __str__(self):
		return str(self.user.first_name) + ' ' + str(self.user.last_name) + ' | ' + str(self.circle)