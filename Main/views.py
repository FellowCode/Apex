from django.shortcuts import render


def index(request):
    return render(request, 'Main/Index.html')

def about(request):
    return render(request, 'Main/About.html')

def test(request):
    pass


