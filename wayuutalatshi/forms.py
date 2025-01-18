from django import forms
from .models import PQRSF

class PQRSFForm(forms.ModelForm):
    class Meta:
        model = PQRSF
        fields = [
            'tipo_solicitud', 
            'correo_electronico', 
            'nombres_apellidos', 
            'cedula', 
            'celular', 
            'descripcion', 
            'archivo'
        ]
        widgets = {
            'tipo_solicitud': forms.Select(attrs={
                'class': 'form-select',
                'style': 'width: 90%;',  # Ajusta el tamaño
            }),
            'correo_electronico': forms.EmailInput(attrs={
                'class': 'form-control',
                'style': 'width: 90%;',  # Ejemplo de ajuste de tamaño
                'placeholder': 'Correo electrónico'
            }),
            'nombres_apellidos': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 90%;',  # Ajusta la longitud del campo
                'placeholder': 'Nombre completo'
            }),
            'cedula': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 90%;',  # Ajusta el tamaño
                'placeholder': 'Cédula'
            }),
            'celular': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 90%;',
                'placeholder': 'Número de celular'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'width: 90%; height: 150px;',  # Ancho y altura personalizados
                'placeholder': 'Describe tu solicitud'
            }),
            'archivo': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'style': 'width: 50%;',  # Ajusta el tamaño
            }),
        }

    archivo = forms.FileField(required=False)