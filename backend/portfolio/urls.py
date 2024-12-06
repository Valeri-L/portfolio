from django.urls import path
from .views import ContactFormView, LeetCodeInfoView

urlpatterns = [
    path('contact/', ContactFormView.as_view(), name='contact-form'),
    path('leetcode/', LeetCodeInfoView.as_view(), name='leetcode-info'),
]
