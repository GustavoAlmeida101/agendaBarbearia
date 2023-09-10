from django.db import models

class agenda(models.Model):
    nome = models.CharField( max_length=50)
    dia = models.DateField()
    hora = models.TimeField()
    servico = models.CharField(max_length=50)
    
    
    def __str__(self) -> str:
        return self.nome
    
