from django.contrib import admin
from .views import*
from django.urls import path,include

urlpatterns = [
   # path('', home),
    #path('student/',post_student),
   # path('update-student/<id>/',update_student),
    #path('delete-student/<id>/',delete_student),
    path('get-book/',get_book),
    path('student/',studentapi.as_view()),
    path('register/',RegisterUser.as_view()),
]
