from rest_framework import generics, permissions

from ..models import Post
from ..permissions import PostPermission
from ..serializers import PostSerializer


class PostListCreateView(generics.ListCreateAPIView):
    """List all posts or create a new post."""

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a specific post."""

    permission_classes = [PostPermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
