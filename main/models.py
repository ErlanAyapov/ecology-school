from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from circle.models import Group
import datetime

now = datetime.datetime.now()

class Article(models.Model):
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	group  = models.ForeignKey(Group, on_delete = models.CASCADE, default = 1)
	body   = models.TextField('Текст')
	date   = models.CharField('Уақыт', max_length = 50, default = 'Белгісіз сайт әкімшісіне хабарлаңыз')

	def __str__(self):
		what = str(self.group) + ' | ' + str(self.author.first_name) + ' ' + str(self.author.last_name)
		return what



