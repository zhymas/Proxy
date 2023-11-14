from django.shortcuts import render, redirect
from .utils import proxy
from .models import ProxyURLObj

def home(request):
    return render(request, 'vpn/home.html')


def create_proxy(request):
    if request.method == 'POST':
        url = request.POST['url']
        if url:
            url_request = ProxyURLObj(user_request=request.user, origin_url=url)
            url_request.save()
            return redirect('home')
    if request.method == "GET":
        url = request.GET.get('url', '')
        if url:
            return proxy(request, url)
    return render(request, 'vpn/index.html')


def last_vpn_connection(request):
    connections = ProxyURLObj.objects.filter(user_request=request.user).order_by('-id')
    
    context = {
        'last_connections': connections
    }
    return render(request, 'users/last_vpn_connection.html', context)
