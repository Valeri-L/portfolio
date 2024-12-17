from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .models import ContactMessage
from django.conf import settings
from django.core.cache import cache
from django.conf import settings

import requests
import json


# LeetCode GraphQL API endpoint and query
LEETCODE_API_URL = settings.LEETCODE_API_URL
LEETCODE_QUERY = settings.LEETCODE_QUERY



class MessageFormView(APIView):
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
        """
        Method:
            GET request that called from the frontend.
        
        Steps:
            1.Define the cache key for LeetCode data)
            2.Check if data is available in cache -> If data exists in cache, return it
            3.If cache miss, fetch fresh data from LeetCode GraphQL -> Cache the data for 25 minutes (1500 seconds) -> Return the fresh data
            4.Handle any errors from the LeetCode API -> if error from Leet Code -> Return 500 
        """



        cache_key = "leetcode_data"
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)
        
        else:
            try:
                response = requests.post(LEETCODE_API_URL, json={"query":LEETCODE_QUERY})
                print(response)
                
                response.raise_for_status()
                data = response.json()

                cache.set(cache_key, data, timeout=5)

                return Response(data, status=status.HTTP_200_OK)

            except requests.RequestException as e:
                return Response({'error': 'Failed to fetch LeetCode data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)