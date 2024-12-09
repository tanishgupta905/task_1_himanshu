from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import Home, SignupView, LoginView, TaskList, LogoutView


urlpatterns = [
    path("", Home.as_view(), name="home_page"),
    path("signup/page/", SignupView.as_view(), name="signup"),
    path("login/page/", LoginView.as_view(), name="login"),
    path("logout/page/", LogoutView.as_view(), name="logout"),
    path("task/list", TaskList.as_view(), name='tasklist')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
