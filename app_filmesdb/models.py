from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Filme(models.Model):
    id_filme = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, unique=True)
    diretor = models.CharField(max_length=100)
    ano = models.IntegerField()
    sinopse = models.TextField(max_length=500, default="Sinopse não disponível")
    imagem = models.URLField(default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXShDI6RpzKwxepFOA0j1nbEdqnLBZUO3CvYhiIVao4Hu_DPD5qW5PywfFAWf755Jvm54&usqp=CAU") # URL da imagem do filme
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])  # Rating do filme
    comentario = models.TextField(max_length=500, default="Sem comentários")  # Comentário do filme
    trailer_url = models.URLField(default="https://www.youtube.com/") 