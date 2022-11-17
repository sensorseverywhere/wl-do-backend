from django.urls import include, path

from .views import ContentDetailAPIView, \
                   ContentListAPIView, \
                   DeleteContentAPIView, \
                   GetContentTypesAPIView, \
                   UpdateContentAPIView, \
                   create_story, \
                   create_story_form, delete_story, \
                   detail_story, \
                   update_story, \
                   delete_story

urlpatterns = [
    path('all/', ContentListAPIView.as_view(), name='content-list'),
    path('detail/<int:pk>/', ContentDetailAPIView.as_view(), name='content-detail'),
    path('delete/<int:pk>/', DeleteContentAPIView.as_view(), name='content-delete'),
    path('update/<int:pk>/', UpdateContentAPIView.as_view(), name='content-update'),
    path('content-types/', GetContentTypesAPIView.as_view()),
    path('story/create/<pk>/', create_story, name="create-story"),
    path('htmx/story/<pk>/udpate/', update_story, name="story-update"),
    path('htmx/story/<pk>/delete/', delete_story, name="story-delete"),
    path('htmx/story/<pk>/', detail_story, name="story-detail"),
    path('htmx/create-story-form/', create_story_form, name="create-story-form")
]
