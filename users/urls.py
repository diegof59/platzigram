"""Users app URL Configuration"""

from django.urls import path

from . import views

urlpatterns = [

    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('me/profile/', views.UpdateProfileView.as_view(), name="update"),
    
    path(
        route = '<str:username>/',
        view = views.UserDetailView.as_view(),
        name = 'details'
    ),
]