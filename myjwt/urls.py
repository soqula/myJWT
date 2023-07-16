from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myjwt.views import (
    MyWightListView,
    )

router = DefaultRouter()
router.register('myjwt', MyWightListView)

urlpatterns = [
    path('', include(router.urls)),
]