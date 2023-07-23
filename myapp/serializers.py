from rest_framework import serializers
from .models import BlogPost,like,user

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = "__all__"

class likeSerializer(serializers.ModelSerializer):
    class Meta:
        model = like
        fields = "__all__"