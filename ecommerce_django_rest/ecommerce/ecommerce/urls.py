from django.contrib import admin
from django.urls import path,include
from website.views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

from website.views import SignupApiView
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Ecommerce API')




urlpatterns = [
        path('admin/', admin.site.urls),
    path('signUp/', SignupApiView.as_view(), name='signUp'),
    path('login/', TokenObtainPairView.as_view(),name='login'),
    path('refresh', TokenRefreshView.as_view(),name='refresh'),
    path('',include('website.urls')),
    path('', schema_view),

]