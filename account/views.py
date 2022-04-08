from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import login

class SignUpView(generic.CreateView):
    model = User
    template_name = 'registration/sign_up.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('')

def sign_up_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect('post_list')

    else:
        return render(request, 'registration/sign_up.html', {'form': UserCreationForm})


