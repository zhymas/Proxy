from django.http import JsonResponse
import requests
from django.http import StreamingHttpResponse
from .models import ProxyURLObj
from django.contrib.auth.models import User

def proxy(request, url):

    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    response = requests.get(url, stream=True)
    response.raise_for_status() 

    if response.status_code == 404:
        return JsonResponse({'error': 'Not Found'})
    

    return StreamingHttpResponse(
        response.raw,
        content_type=response.headers.get('content-type'),
        status=response.status_code,
        reason=response.reason
    )
