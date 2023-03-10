from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views


urlpatterns = [
    path('', include('djoser.urls.jwt')),
]

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', views.CommentViewSet,
                basename="comments")
router.register(r'follow', views.Following, basename='follow')

urlpatterns += router.urls
