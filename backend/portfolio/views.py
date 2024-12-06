from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .models import ContactMessage
from django.conf import settings
import requests




class ContactFormView(APIView):
    def post(self, request):
        data = request.data
        try:
            # Save message to the database
            message = ContactMessage.objects.create(
                name=data['name'],
                email=data['email'],
                phone=data.get('phone', ''),#phone is optional
                message=data['message']
            )

            # Send email notification
            send_mail(
                subject=f"New Contact Form Submission from {message.name}",
                message=f"""
                Name: {message.name}
                Email: {message.email}
                Phone: {message.phone or 'Not provided'}
                Message: {message.message}
                """,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=False
            )

            return Response({'success': 'Message sent successfully!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class LeetCodeInfoView(APIView):
    def get(self, request):
        try:
            # Simulate fetching LeetCode info
            leetcode_data = {
                "username": "your_username",
                "total_problems_solved": 150,
                "ranking": 2000
            }
            return Response(leetcode_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Failed to fetch LeetCode data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)