from django.urls import path
from . import views
from .views import PostListview, PostDetailsView, PostCreateView

urlpatterns = [
    path('', PostListview.as_view(), name="blog home"),
    path('post/<int:pk>', PostDetailsView.as_view(), name="post-details"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('about/', views.about, name="blog about"),

]
