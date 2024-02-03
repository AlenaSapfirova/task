from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import User, Post, Subscribtion
from.serializers import PostSerializer, UserSerializer, SubscribSerializer
from.pagination import CustomPagination

class PostAPIView(APIView):
    serializer_class = PostSerializer

    def post(self, request):
        author = self.request.user
        serializer = PostSerializer(author,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        posts = Post.objects.filter(author=request.user)[:500]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class PostDetailAPIView(APIView):
    serializer_class = PostSerializer

    def patch(self, request, **kwargs):
        pk=self.kwargs.get('id')
        post = get_object_or_404(Post, id=pk, author=request.user)
        serializer = PostSerializer(post, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, **kwargs):
        pk = self.kwargs.get('id')
        post = get_object_or_404(Post, id=pk, author=request.user)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    @action(serializer_class=SubscribSerializer,detail=False, methods=['get'])
    def subscriptions(self, request):
        user = request.user
        query = User.objects.filter(author__user=user)
        serializer = SubscribSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, serializer_class=SubscribSerializer, methods=['post', 'delete'])
    def subscribe(self, request, id):
        user = self.request.user
        if request.methods == "POST":
            author = get_object_or_404(User, id=id)
            if Subscribtion.objects.filter(user=self.request.user, author=author).exists():
                return ValidationError('Подписка уже существует')
            Subscribtion.objects.create(user=self.request.user, author=author)
            serializer = self.get_serializer(author)
            return Response(serializer.data, status=status.HTTP_200_OK)
        author = get_object_or_404(User, id=id)
        user = self.request.user
        subscribe = get_object_or_404(Subscribtion, user=user, author=author)
        subscribe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

