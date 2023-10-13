from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def staff_dshbd_view(request):
    return render(request, 'staff_dshbd.html')

def studnt_dshbd_view(request):
    return render(request, 'studnt_dshbd.html')

