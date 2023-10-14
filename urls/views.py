from django.http import JsonResponse
from .models import URL
from django.shortcuts import redirect


def redirect_to_full_url(request, short_url):
    try:
        my_model = URL.objects.get(shorturl=short_url)
        return redirect(my_model.Full_url)
    except URL.DoesNotExist:
        response_data = {
            'error': 'URL not found',
            'message': 'Please enter a valid URL.'
        }
        return JsonResponse(response_data, status=404)
