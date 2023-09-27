from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name="court_system"
urlpatterns = [
    path("",views.home,name="landingpage"),
    path("client_login",views.Login,name="login"),
    path("home",views.userlanding,name="home"),
    path("client_save",views.client_save,name="client_save"),
]
