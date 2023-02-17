from django.urls import path, include
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()

router.register(r'profile', WriterProfileViewSet)
router.register(r'news', NewsViewSet)
router.register(r'comment', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]