'''
Created on Apr 13, 2020

@author: shamim
'''

from django.urls.conf import path
from student import views

urlpatterns=[
    path('addstudent/',views.addstudent, name="addstudent"),
    path('addstudent/showdept/<email>',views.showdept, name="stdid"),
    path('addstudent/showdept/<email>/<deptname>',views.adddept,name="deptadd"),
    path('pdf/', views.get, name='pdf'),
    path('csv/',views.csv_database_write,name='csv')
    
    ]
