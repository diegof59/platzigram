"""Users app URL Configuration"""

from django.urls import path

from . import views

urlpatterns = [

    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup_view, name="signup"),
    path('me/profile/', views.update_profile, name="update"),
    
    path(
        route = '<str:username>/',
        view = views.UserDetailView.as_view(),
        name = 'details'
    ),
]