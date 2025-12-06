from django.db import models
from django.conf import settings

class LifeDimension(models.Model):
    """
    As áreas da vida: Saúde, Fé, Trabalho, Família, etc.
    """
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    color = models.CharField(max_length=20, default="#00B050") # Cor do tema (Hex)
    icon = models.CharField(max_length=50, default="heart") # Nome do ícone Lucide

    def __str__(self):
        return self.name

class Milestone(models.Model):
    """
    Marcos de Vida (Antigo MyLife).
    Momentos que definem a história do usuário.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='milestones')
    title = models.CharField("Título", max_length=200)
    date = models.DateField("Data do Marco")
    description = models.TextField("Descrição", blank=True)
    dimension = models.ForeignKey(LifeDimension, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='milestones/', null=True, blank=True)
    
    is_private = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

class JournalEntry(models.Model):
    """
    Diário de Consciência (Antigo Journal).
    Registro diário de gratidão e estado emocional.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    mood_level = models.IntegerField(default=5) # 1 a 10
    gratitude_1 = models.CharField(max_length=255, blank=True)
    gratitude_2 = models.CharField(max_length=255, blank=True)
    gratitude_3 = models.CharField(max_length=255, blank=True)
    reflection = models.TextField("Reflexão do dia", blank=True)

    class Meta:
        verbose_name_plural = "Journal Entries"
        unique_together = ('user', 'date')

    def __str__(self):
        return f"Diário de {self.user} - {self.date}"

class Goal(models.Model):
    """
    Metas e Sonhos (Antigo Goals).
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    dimension = models.ForeignKey(LifeDimension, on_delete=models.SET_NULL, null=True)
    deadline = models.DateField(null=True, blank=True)
    progress = models.IntegerField(default=0) # 0 a 100%
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title