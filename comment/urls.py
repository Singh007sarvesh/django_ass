from django.urls import path
from comment.views import CommentView

urlpatterns = [
    path('comments/', CommentView.as_view(), name='comments'),
    path('comments/<int:id>', CommentView.as_view(), name='comments'),
]