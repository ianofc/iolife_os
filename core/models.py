from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    O 'CORE' do usuário.
    Substitui o modelo padrão do Django.
    """
    bio = models.TextField("Declaração de Vida", blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    
    # Gamificação da Vida (Legacy System)
    level = models.PositiveIntegerField(default=1)
    xp = models.PositiveIntegerField(default=0)
    
    # Configurações de Privacidade (Granular)
    is_public = models.BooleanField(default=True)
    
    # Dados Existenciais
    life_phase = models.CharField("Fase da Vida", max_length=100, blank=True, help_text="Ex: Construindo Carreira, Pai de Primeira Viagem")

    def __str__(self):
        return self.username