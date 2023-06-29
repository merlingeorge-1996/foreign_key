from django.urls import path,include
from .import views
urlpatterns = [
    path('', views.home,name='home'),
    path('add_course',views.add_course,name="add_course"),
    path('add_coursedb',views.add_coursedb,name="add_coursedb"),
    path('add_student',views.add_student,name="add_student"),
    path('add_studentdb',views.add_studentdb,name="add_studentdb"),
    path('show_details',views.show_details,name="show_details"),
    path('editstudent/<int:pk>',views.editstudent,name='editstudent'),
    path('edit_student_details/<int:pk>',views.edit_student_details,name='edit_student_details'),
    path('deletestudent/<int:pk>',views.deletestudent,name='deletestudent'),




]