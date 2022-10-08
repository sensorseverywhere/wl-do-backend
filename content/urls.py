from django.urls import include, path

from .views import PageAPIView, PageListAPIView

urlpatterns = [
    path('all/', PageListAPIView.as_view(), name='content-list'),
    path('<string>/', PageAPIView.as_view(), name='content-detail'),
]
