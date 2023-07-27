from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('add_todo/',views.add_todo),
    path('delete_todo/<int:id>',views.delete_todo)
]