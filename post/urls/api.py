from django.urls import path

from ..views.api import PostListCreateView, PostRetrieveUpdateDestroyView

app_name = "post_api"

urlpatterns = [
    path("", PostListCreateView.as_view(), name="post-list"),
    path("<int:pk>/", PostRetrieveUpdateDestroyView.as_view(), name="post-detail"),
]
