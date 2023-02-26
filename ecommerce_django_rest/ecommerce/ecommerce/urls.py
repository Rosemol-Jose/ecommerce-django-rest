from django.contrib import admin
from django.urls import path,include
from website.views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signUp/', SignupApiView.as_view(), name='signUp'),
    path('login/', TokenObtainPairView.as_view(),name='login'),
    path('refresh', TokenRefreshView.as_view(),name='refresh'),
    path('logout/', logout,name='logout'),
    path('',include('website.urls')),

]