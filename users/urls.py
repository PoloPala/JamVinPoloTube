from django.contrib.auth import views as auth_views
from django.urls import path
from .views import user_login, signup

urlpatterns = [
    path('login/', user_login, name='login'),
    #path('logout/', user_logout, name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Built-in LogoutView
    path('signup/', signup, name='signup'),
]
