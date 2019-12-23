from django.shortcuts import render
from .forms import RegistrationForm
from entries.models import Profile
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful, you can log in')
            
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)
