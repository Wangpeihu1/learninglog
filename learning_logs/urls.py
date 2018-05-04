#定义learning_logs的URL模式
from django.urls import path, re_path
from . import views
app_name = 'learning_logs'
urlpatterns = [
	#主页
	path('',views.index,name='index'),
	#显示所有主题
	path('topics/',views.topics,name='topics'),
	#显示单个主题
	re_path('topics/(?P<topic_id>\d+)/',views.topic,name='topic')
]
