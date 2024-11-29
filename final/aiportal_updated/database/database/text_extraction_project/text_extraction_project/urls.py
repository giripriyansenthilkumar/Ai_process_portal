from django.contrib import admin
from django.urls import path
from text_extraction import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload_document, name='upload_document'),
]
