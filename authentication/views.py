from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View

from utils.utils import anonymous_required, dispatch_decorator


@dispatch_decorator(anonymous_required)
class RegisterView(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        if not User.objects.filter(username=request.POST['username']).exists():
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            return redirect('/')
        return render(request, 'register.html', {'message': 'Account could not be created with received data.'})


@dispatch_decorator(anonymous_required)
class LoginView(View):

    def get(self, request):
        return render(request,'login.html')

    def post(self, request):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return render(request,'login.html', {'message': 'Account has been disabled.'})
        return render(request,'login.html', {'message': 'Username/password combination invalid.'})


@login_required
def logout_view(request):
    logout(request)
    return redirect('feed')