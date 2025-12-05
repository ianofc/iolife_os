from django.db import models
from django.conf import settings

class Log(models.Model):
    """
    Antigo 'Post'. Agora é um Registro de Vida.
    Pode ser um texto, uma foto, um vídeo ou um marco.
    """
    AREA_CHOICES = [
        ('social', 'Social'),
        ('trabalho', 'Trabalho'),
        ('fe', 'Fé'),
        ('familia', 'Família'),
        ('saude', 'Corpo & Mente'),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='logs')
    content = models.TextField("Conteúdo")
    image = models.ImageField(upload_to='logs/', null=True, blank=True)
    video = models.FileField(upload_to='logs_video/', null=True, blank=True)
    
    area = models.CharField(max_length=20, choices=AREA_CHOICES, default='social')
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Métricas (Vals e Echos)
    val_count = models.PositiveIntegerField(default=0) # Likes
    echo_count = models.PositiveIntegerField(default=0) # Comments

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author} - {self.get_area_display()} - {self.created_at}"