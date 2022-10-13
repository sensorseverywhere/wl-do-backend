from django.urls import include, path

from .views import ContentAPIView, ContentListAPIView, DeleteContentAPIView, GetContentTypesAPIView, UpdateContentAPIView

urlpatterns = [
    path('all/', ContentListAPIView.as_view(), name='content-list'),
    path('detail/<string>/', ContentAPIView.as_view(), name='content-detail'),
    path('delete/<int:pk>/', DeleteContentAPIView.as_view(), name='content-delete'),
    path('update/<int:pk>/', UpdateContentAPIView.as_view(), name='content-update'),
    path('content-types/', GetContentTypesAPIView.as_view()),
]
