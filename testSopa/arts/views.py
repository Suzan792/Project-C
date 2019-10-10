from django.http import HttpResponse
from django.shortcuts import render

from .models import Arts

# Create your views here.
def arts_list(request):
    arts = Arts.objects.all()
    output = ', '.join([str(arts) for art in arts])
    return HttpResponse(output)
