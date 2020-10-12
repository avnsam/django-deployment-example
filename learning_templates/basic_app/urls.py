from django.urls import path
from basic_app import views

#TEMPLATE TAGGING

# We're creating a namespace below called 'basic_app'. This tells django we want to use template tagging on basic_app
app_name = 'basic_app'   

urlpatterns= [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),

]