from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name="court_system"
urlpatterns = [
    path("",views.home,name="home"),
    path("client_signup",views.client_signup,name="client_signup"),
    path("client_login",views.client_login,name="client_login"),
    path("client_save",views.client_save,name="client_save"),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
