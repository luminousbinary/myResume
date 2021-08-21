from django.shortcuts import render

# Create your views here.

def resumePage(request):
    return render(request, 'resumePage.html', {}) 