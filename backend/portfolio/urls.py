from django.urls import path
from .views import MessageFormView, LeetCodeInfoView

urlpatterns = [
    path('message', MessageFormView.as_view(), name='message-form'),
    path('leetcode/', LeetCodeInfoView.as_view(), name='leetcode-info'),
]
