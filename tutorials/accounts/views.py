from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request,'accounts/home.html')
def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home:home'))
    else:
        form = UserCreationForm()
    args = {'form': form}
    return render(request, 'accounts/reg_form.html', args)
