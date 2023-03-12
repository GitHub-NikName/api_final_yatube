from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


from posts import models


class Group(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = '__all__'


class Post(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = models.Post
        fields = '__all__'
        read_only_fields = ('author',)


class Comment(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = models.Comment
        fields = '__all__'
        read_only_fields = ('author', 'post')


class Follow(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=models.User.objects.all()
    )

    class Meta:
        model = models.Follow
        fields = ('user', 'following')
        validators = [
            UniqueTogetherValidator(
                queryset=models.Follow.objects.all(),
                fields=('user', 'following'),
                message='Подписка на автора уже есть.'
            )
        ]

    def validate_following(self, following):
        if self.context['request'].user == following:
            raise serializers.ValidationError(
                'Нельзя подписаться на себя.')
        return following
