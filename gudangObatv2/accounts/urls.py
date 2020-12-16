from django.conf.urls import url, include
from accounts import views
from .views import GoogleLogin

urlpatterns = [
    url(r'^login/', views.loginPage, name="login"),
    url(r'^register/', views.registerPage, name="register"),
    url(r'^logout/', views.logoutUser, name="logout"),
    url(r'^auth/', include('dj_rest_auth.urls')),
    url(r'^social-login/google/', GoogleLogin.as_view(), name='google_login'),
]