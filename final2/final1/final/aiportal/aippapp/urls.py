from django.urls import path
from . import views

urlpatterns =[
    path("",views.home, name="home"),
    path("app1/",views.app1, name="app1"),
    path("app2/",views.app2, name="app2"),
    path("app3/",views.app3, name="app3"),
    path("app4/",views.app4, name="app4"),

]