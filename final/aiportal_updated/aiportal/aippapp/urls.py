from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('login_user/', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('register_user/', views.register_user, name='register_user'),
    path('success/', views.success, name='success'),
    path('app1/', views.app1, name='app1'),
    path('save_applicant/', views.save_applicant, name='save_applicant'),
    path('app2/', views.app2, name='app2'),
    path('save_family_details/', views.save_family_details, name='save_family_details'), # Add this line
    path('app3/', views.app3, name='app3'),
    path('save_bank_details/', views.save_bank_details, name='save_bank_details'),
    path('app4/', views.app4, name='app4'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
