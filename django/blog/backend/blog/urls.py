from django.urls import path
from .views import (BlogView,PostDetailView)

app_name='blog'

urlpatterns = [
    path('',BlogView.as_view(),name='home'),
    path('<slug:slug>/',PostDetailView.as_view(),name='post-detail'),
]
