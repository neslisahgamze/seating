"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

from api.views import UserViewSet
from api.views import TicketViewSet
from api.views import CategoryViewSet
from api.views import SeatViewSet
from api.views import SectionViewSet
from api.views import EventViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/tickets', TicketViewSet)
router.register(r'api/category', CategoryViewSet)
router.register(r'api/seats', SeatViewSet)
router.register(r'api/sections', SectionViewSet)
router.register(r'api/events', EventViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/events/<int:pk>/seats', EventViewSet.as_view({"post": "find_seats"})),
    path(r'api/users/<int:userId>/tickets', UserViewSet.as_view({"get": "tickets"})),
    # path(r'api/users/<int:eventId>/', UserViewSet.as_view({"get": "ticket"})),
    path('openapi/', get_schema_view(
        title="School Service",
        description="API for developers who would love to use our service in a School project" 
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]
