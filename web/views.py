from django.shortcuts import render

def home(request):
    """Página principal"""
    context = {
        'titulo': 'Smart Assisted Cane for the Visually Impaired',
        'subtitulo': 'Next-Generation Urban Mobility & Health 4.0 Assistive Technology',
        'resumen': 'An innovative IoT smart cane designed to detect elevated obstacles, empowering visually impaired individuals with real-time haptic feedback and dynamic spatial awareness.'
    }
    return render(request, 'home.html', context)

def plantilla1(request):
    """Página 1: The Need"""
    context = {
        'titulo': 'Relevance of the Need',
        'subtitulo': 'Addressing Critical Public Health and Accessibility Challenges',
    }
    return render(request, 'plantilla1.html', context)

def plantilla2(request):
    """Página 2: Architecture"""
    context = {
        'titulo': 'Technical Architecture',
        'subtitulo': 'IoT Hardware, Sensor Logic & Autonomous Guidance',
    }
    return render(request, 'plantilla2.html', context)

def plantilla3(request):
    """Página 3: Health 4.0"""
    context = {
        'titulo': 'Health 4.0 Integration',
        'subtitulo': 'Convergence of IoT, AI, Robotics, Additive Manufacturing & Cloud',
    }
    return render(request, 'plantilla3.html', context)

def plantilla4(request):
    """Página 4: Impact & Feasibility"""
    context = {
        'titulo': 'User Impact & Feasibility',
        'subtitulo': 'Human-Centered Benefits & Academic Implementation Strategy',
    }
    return render(request, 'plantilla4.html', context)

def contacto(request):
    enviado = False
    if request.method == 'POST':
        nombre = request.POST.get('name')
        correo = request.POST.get('email')
        necesidades = request.POST.get('needs')
        
        print("=========================================")
        print(f"NUEVA SOLICITUD DE: {nombre} ({correo})")
        print(f"NECESIDADES: {necesidades}")
        print("=========================================")
        
        enviado = True

    return render(request, 'contacto.html', {'enviado': enviado})