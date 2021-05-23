from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

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
            'form': form
        }
        return render(request, 'index.html', context)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signUp.html'
