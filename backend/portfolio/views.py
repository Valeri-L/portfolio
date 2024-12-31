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
from portfolio.api_fetch import APIFetch
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from portfolio.serializers import SendMessageSerializer





class MessageFormView(APIView):
    throttle_classes = [AnonRateThrottle]

    def post(self, request):
        data = request.data

        # Verify reCAPTCHA token
        recaptcha_token = data.get('recaptchaToken')
        if not recaptcha_token:
            return Response({'error': 'reCAPTCHA token is missing.'}, status=status.HTTP_400_BAD_REQUEST)

        recaptcha_secret = settings.RECAPTCHA_SECRET_KEY  # Set this in your settings
        recaptcha_url = "https://www.google.com/recaptcha/api/siteverify"

        try:
            recaptcha_response = requests.post(recaptcha_url, data={
                'secret': recaptcha_secret,
                'response': recaptcha_token,
            })
            recaptcha_result = recaptcha_response.json()

            if not recaptcha_result.get('success'):
                return Response({'error': 'Invalid reCAPTCHA token.'}, status=status.HTTP_400_BAD_REQUEST)

            # Save message to the database
            serializer = SendMessageSerializer(data=data)
            if serializer.is_valid():
                message = ContactMessage.objects.create(
                    name=data['name'],
                    email=data['email'],
                    phone=data.get('phone', ''),  # phone is optional
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
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )

                return Response({'success': 'Message sent successfully!'}, status=status.HTTP_200_OK)
            else:
                return Response({'error':'invalid fields received'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
            
        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class LeetCodeInfoView(APIView):
    throttle_classes = [AnonRateThrottle]

    def get(self, request):
        """
        Method:
            GET request that is called from the frontend.
        
        Steps:
            1. Define the cache key for LeetCode data.
            2. Check if data is available in cache -> If data exists in cache, return it.
            3. If cache miss, fetch fresh data from LeetCode GraphQL -> Cache the data for 25 minutes (1500 seconds) -> Return the fresh data.
            4. Handle any errors from the LeetCode API -> if error from LeetCode -> Return 500.
        """
        cache_key = "leetcode_data"
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)
        
        else:
            try:
                # Fetch the data and display the results
                leetcode_data = APIFetch.fetch_leetcode_data()
               
                # Cache the filtered data for 25 minutes
                cache.set(cache_key, leetcode_data, timeout=3600)

                # Return the filtered data
                return Response(leetcode_data, status=status.HTTP_200_OK)

            except requests.RequestException as e:
                # Handle errors if the request fails
                return Response({'error': 'Failed to fetch LeetCode data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)