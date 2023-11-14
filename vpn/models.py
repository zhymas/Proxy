from django.db import models
from django.contrib.auth.models import User


class ProxyURLObj(models.Model):
    user_request = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proxy_requests', )
    origin_url = models.URLField()
    
    def __str__(self):
        return self.origin_url
