'''
Created on Apr 18, 2020

@author: shamim
'''

from accounts import views
from django.urls.conf import path
urlpatterns=[
   path('register/', views.register, name='register'),
   path('login/', views.loginuser, name='login'),
   path('logout/',views.logoutuser, name='logout'),
   path('',views.home, name='home'),
    
    ]