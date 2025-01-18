from django.shortcuts import render
from django.urls import path
from . import views

def index(request):
    return render(request, 'index.html')


from django.shortcuts import render

def servicios(request):
    servicios = [
        {"nombre": "Enfermería", "descripcion": "Atención de calidad en procedimientos de enfermería básicos y avanzados."},
        {"nombre": "Ginecobstetricia", "descripcion": "Cuidado integral para la salud de la mujer en todas las etapas de su vida."},
        {"nombre": "Medicina General", "descripcion": "Diagnóstico y tratamiento inicial para diversas condiciones de salud."},
        {"nombre": "Medicina Interna", "descripcion": "Especializada en la prevención, diagnóstico y tratamiento de enfermedades en adultos."},
        {"nombre": "Nutrición y Dietética", "descripcion": "Planes nutricionales personalizados para mejorar tu calidad de vida."},
        {"nombre": "Odontología General", "descripcion": "Servicios de salud bucal para mantener dientes y encías saludables."},
        {"nombre": "Oftalmología", "descripcion": "Diagnóstico y tratamiento de enfermedades oculares y corrección visual."},
        {"nombre": "Optometría", "descripcion": "Exámenes visuales y prescripción de lentes para mejorar tu visión."},
        {"nombre": "Pediatría", "descripcion": "Atención médica para niños, desde recién nacidos hasta adolescentes."},
        {"nombre": "Psicología", "descripcion": "Apoyo psicológico para promover la salud mental y el bienestar emocional."},
        {"nombre": "Otras Consultas Generales", "descripcion": "Atención para condiciones generales que requieren orientación médica."},
        {"nombre": "Vacunación", "descripcion": "Protección contra enfermedades mediante esquemas de vacunación actualizados."},
        {"nombre": "Laboratorio Clínico", "descripcion": "Análisis clínicos para un diagnóstico médico preciso y oportuno."},
        {"nombre": "Toma de Muestras de Laboratorio Clínico", "descripcion": "Recolección profesional de muestras para análisis especializados."},
        {"nombre": "Servicio Farmacéutico", "descripcion": "Atención para la entrega y asesoría de medicamentos."},
        {"nombre": "Laboratorio Citologías Cérvico-Uterinas", "descripcion": "Realización de citologías para el diagnóstico de enfermedades cervicales."},
        {"nombre": "Terapia Ocupacional", "descripcion": "Rehabilitación para mejorar la capacidad funcional en actividades cotidianas."},
        {"nombre": "Fisioterapia", "descripcion": "Tratamientos para recuperar la movilidad y aliviar el dolor muscular o articular."},
        {"nombre": "Fonoaudiología y/o Terapia del Lenguaje", "descripcion": "Rehabilitación y tratamiento de trastornos del habla y la comunicación."},
        {"nombre": "Imágenes Diagnósticas - Ionizantes", "descripcion": "Estudios de diagnóstico por imágenes mediante radiografías y otras técnicas ionizantes."},
        {"nombre": "Toma de Muestras de Cuello Uterino y Ginecológicas", "descripcion": "Recolección de muestras para el diagnóstico de condiciones ginecológicas."},
    ]
    return render(request, 'servicios.html', {'servicios': servicios})


from django.http import JsonResponse
from django.shortcuts import render
from .forms import PQRSFForm
from .models import PQRSF

def contacto(request):
    form = PQRSFForm()
    return render(request, 'contacto.html', {'form': form})

def guardar_pqrsf(request):
    if request.method == 'POST':
        form = PQRSFForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Su solicitud fue enviada Correctamente.'})
        else:
            return JsonResponse({'success': False, 'message': 'Error al guardar el formulario.', 'errors': form.errors})
    return JsonResponse({'success': False, 'message': 'Método no permitido.'})
