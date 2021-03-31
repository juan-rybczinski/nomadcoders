from django.shortcuts import render
from django.views import View
from . import forms


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm(initial={"email": "rybczinski0726@gmail.com"})
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, "users/login.html", {"form": form})
