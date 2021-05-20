from django.shortcuts import render, redirect
from pictures.models import photo
from .forms import NewPhoto


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = NewPhoto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    else:
        form = NewPhoto()
        photos = photo.objects.all()
        context = {
            'photos': photos,
            'form' : form
        }
        return render(request, 'index.html', context)


