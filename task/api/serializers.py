from rest_framework import serializers
from .models import User, Post, Subscribtion

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Post
        fields = ['header', 'body','id', 'author']
    

class PostSubscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['header', 'body', 'is_read_it', 'id']

class SubscribSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(read_only=True)
    posts = serializers.SerializerMethodField()
    is_subscribed = serializers.BooleanField(default=True)

    class Meta:
        model = Subscribtion
        fields = ['username', 'posts', 'is_subscribed']

    def get_posts(self, obj):
        posts = obj.author_post.all()
        request = self.context['request']
        serializer = PostSubscribeSerializer(posts, many=True, context={'request':request})
        return serializer.data

    

class UserSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'is_subscribed']


    def get_is_subscribed(self, obj):
        print(obj)
        user = self.context['request'].user
        return Subscribtion.objects.filter(user=user, author=obj).exists()
    
    