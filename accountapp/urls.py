from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),  

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),  
    path('logout/', LogoutView.as_view(template_name='accountapp/logout.html'), name='logout'),  

    path('create/', AccountCreateView.as_view(), name='create'),    
]
