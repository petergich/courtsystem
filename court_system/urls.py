from django.urls import path
from . import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.home,name="landingpage"),
    path("clienthome",views.clientlogin,name="try"),
    path("lawyerhome",views.lawyerlogin,name="try1"),
    path("client_login",views.Login,name="login"),
    path("client_save",views.client_save,name="client_save"),
]
