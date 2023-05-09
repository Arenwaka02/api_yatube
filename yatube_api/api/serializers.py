from rest_framework import serializers
from posts.models import Group, Post, Comment
from rest_framework.relations import PrimaryKeyRelatedField, SlugRelatedField



class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'slug', 'description',)
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    group = PrimaryKeyRelatedField(
        required=False,
        queryset=Group.objects.all()
    )

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group',)
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')
    post = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created',)
        model = Comment