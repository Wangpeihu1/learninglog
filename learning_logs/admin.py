from django.contrib import admin

from learning_logs.models import Topic,Entry
admin.site.register(Topic)
admin.site.register(Entry)

from Pizzas.models import Pizza,Topping
admin.site.register(Pizza)
admin.site.register(Topping)
