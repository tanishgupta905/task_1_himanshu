from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .forms import SignupForms, LoginForms, TaskForm, CommentForm
from django.contrib.auth import login, logout, authenticate
from .models import User, Task, Comment


# Home page
class Home(TemplateView):
    template_name = "index.html"


class SignupView(View):
    template_name = "signup.html"

    def get(self, request):
        form = SignupForms()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = SignupForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request, self.template_name, {"form": form})


class LoginView(TemplateView):
    template_name = "login.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("tasklist")
        form = LoginForms()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = LoginForms(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("tasklist")
        return render(request, self.template_name, {"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("home_page")


class TaskList(TemplateView):
    template_name = "tasklist.html"
