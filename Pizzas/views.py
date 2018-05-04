from django.shortcuts import render

def index(request):
	#Pizzas主页
	return render(request,'Pizzas/index.html')
