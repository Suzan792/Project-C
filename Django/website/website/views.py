from django.shortcuts import get_object_or_404, render
def index(request):
    return render(request,'index.html')
def contact_page(request):
    return render(request,'contact.html')
