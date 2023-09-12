from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


def contact_info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'name: {name}, email: {email}, message: {message}')
    return render(request, 'catalog/contact_info.html')