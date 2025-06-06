"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

#NEW
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todos.views import TodoViewSet
from rest_framework.authtoken.views import obtain_auth_token
from todos.views import SecureHelloView

router = DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
     path('admin/', admin.site.urls),
     path('api-token-auth/', obtain_auth_token),
     path('secure-hello/', SecureHelloView.as_view()),
]