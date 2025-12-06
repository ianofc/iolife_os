from django.db import models
from django.conf import settings

class Tribe(models.Model):
    """
    Antigas Comunidades/Hubs.
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    cover = models.ImageField(upload_to='tribes/', null=True, blank=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='tribes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Link(models.Model):
    """
    Conexões entre usuários (Amigos/Seguidores).
    """
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('active', 'Conectado'),
        ('blocked', 'Bloqueado'),
    ]
    
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_links')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_links')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('sender', 'receiver')

    def __str__(self):
        return f"{self.sender} -> {self.receiver} ({self.status})"