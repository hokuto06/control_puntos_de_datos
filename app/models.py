from django.db import models

class Punto(models.Model):
    ESTADO_CHOICES = [
        ('finalizado', 'Finalizado'),
        ('pendiente', 'Pendiente'),
        ('reservada', 'Reservada'),
    ]

    numero_punto = models.AutoField(primary_key=True)
    area = models.CharField(max_length=200)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    comentarios = models.TextField(blank=True, null=True)
    certificado = models.BooleanField(default=False)

    def __str__(self):
        return f"Punto {self.numero_punto}"
