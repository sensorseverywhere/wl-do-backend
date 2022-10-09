from django.urls import include, path

from .views import PageAPIView, PageListAPIView, DeleteContentAPIView

urlpatterns = [
    path('all/', PageListAPIView.as_view(), name='content-list'),
    path('<string>/', PageAPIView.as_view(), name='content-detail'),
    path('delete/<int:pk>/', DeleteContentAPIView.as_view(), name='content-delete'),
]
