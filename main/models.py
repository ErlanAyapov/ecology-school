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

	class Meta:
		verbose_name = 'Клуб жаңалықтары'
		verbose_name_plural = 'Клуб жаңалықтары'


class Comment(models.Model):

	post   = models.ForeignKey(Article, on_delete = models.CASCADE)
	author = models.ForeignKey(User, on_delete = models.CASCADE) 
	comment = models.TextField('Пікір')

	def __str__(self):
		return str(self.author.first_name)

	class Meta:
		verbose_name = 'Пікір'
		verbose_name_plural = 'Пікірлер'



class Post(models.Model):

	body 		 = models.TextField('Мәтін')
	author 		 = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор')
	image_base64 = models.TextField('Сурет (Base64)', blank = True)
	youtube_link = models.TextField('Видео (Ютуб)', blank = True)
	date  		 = models.CharField('Уақыт', max_length = 50, default = 'Белгісіз сайт әкімшісіне хабарлаңыз')

	def __str__(self):
		return str(self.author.first_name) + str(self.author.last_name)

	class Meta:
		verbose_name = 'жаңалық'
		verbose_name_plural = 'жаңалықтар'