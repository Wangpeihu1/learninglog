#为应用程序users定义URL模式
from django.urls import path, re_path
from django.contrib.auth.views import login

from . import views
app_name = 'users'
urlpatterns = [
	#登陆页面
	path('login/',login,{'template_name':'users/login.html'},name='login'),
	path('logout/',views.logout_view,name='logout'),
	path('register/',views.register,name='register')
]