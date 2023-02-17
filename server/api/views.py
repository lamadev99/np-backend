from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from api.models import *
from api.serializers import *
from api.renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from .pagination import MyPagination


# Create your views here.

class WriterProfileViewSet(viewsets.ModelViewSet):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    queryset = Writer.objects.all()
    serializer_class = WriterPorfileSerializer
    if queryset.count() > 0:
        pagination_class = MyPagination

class NewsViewSet(viewsets.ModelViewSet):
    renderer_classes = [UserRenderer]
    queryset = News.objects.all().order_by('-updated_at')
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'subCategory', 'keywords']
    search_fields = ['^category', '^subCategory', '^title', '^keywords']
    if queryset.count() > 0:
        pagination_class = MyPagination


class CommentViewSet(viewsets.ModelViewSet):
    renderer_classes = [UserRenderer]
    queryset = Comment.objects.all().order_by('-cId')
    serializer_class = CommentSerializer
    if queryset.count() > 0:
        pagination_class = MyPagination