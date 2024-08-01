from django.urls import path
from . import views

urlpatterns = [
     path('login/', views.user_login_view, name="login"),
     path('signup/', views.SignUpView.as_view(), name='signup'),
     path('app/', views.app_running, name='app'),
     path('addperson/', views.add_person , name='add'),
     path('allpersons/', views.get_all_persons, name='allpersons'),
     path('delete/', views.DeleteUsernameView.as_view(), name='delete'),
     path('land/', views.landing_view, name = 'land')
]