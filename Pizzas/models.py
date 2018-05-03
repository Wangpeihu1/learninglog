from django.db import models

class Pizza(models.Model):
	name = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add= True)
	def __str__(self):
		#返回模型的字符串表示
		return self.name

class Topping(models.Model):
	#学到的某个主题的具体知识
	pizza = models.ForeignKey('Pizza',on_delete=models.CASCADE)
	name = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		#返回模型耳朵字符串表示
		return self.name
