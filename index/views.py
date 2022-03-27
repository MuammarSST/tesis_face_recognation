from django.shortcuts import render

# Create your views here.
from index.models import Data_user



def indexAction(request):
    hasil = Data_user.objects.all()
    data = {
        'data': hasil,
    }
    return render(request, 'index_page.html', data)