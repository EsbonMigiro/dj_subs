from django.urls import path
from . views import CommentView, SerializerView
urlpatterns = [
    path('s/', CommentView.as_view(), name='comment'),
    path('login_s/', SerializerView.as_view(), name='login_s')

]