from django.db import models

class PQRSF(models.Model):
    TIPO_SOLICITUD_CHOICES = [
        ('peticion', 'Petición'),
        ('queja', 'Queja'),
        ('reclamo', 'Reclamo'),
        ('sugerencia', 'Sugerencia'),
        ('felicitacion', 'Felicitación'),
    ]

    tipo_solicitud = models.CharField(
        max_length=255,
        choices=TIPO_SOLICITUD_CHOICES,
    )
    correo_electronico = models.EmailField()
    nombres_apellidos = models.CharField(max_length=255)
    cedula = models.CharField(max_length=20)
    celular = models.CharField(max_length=15)
    descripcion = models.TextField()
    archivo = models.FileField(upload_to='uploads/')
    
    class Meta:
        db_table = 'solicitudes'  # Nombre explícito de la tabla

    def __str__(self):
        return self.nombres_apellidos
