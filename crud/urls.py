from django.urls import path 
from .views import home,add_student,edit_student,delete_student
 
 
 
urlpatterns = [
    path('',home,name='home'),
    path('add/',add_student,name='add'),
    path('edit/<int:id>/',edit_student,name='edit'),
    path('delete/<int:id>/',delete_student,name='delete'),
]