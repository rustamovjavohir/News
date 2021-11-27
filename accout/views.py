from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse_lazy

from accout.mappers.dto_to_model_mapper import to_user_model, to_employee_model
from accout.mappers.request_to_dto_mapper import request_to_dto
from qalampir.util.base_utils import save_file
from qalampir.util.email_utils import send_verification_token


def sign_in(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next = request.GET.get('next')
            return redirect(next or '/')
        else:
            messages.error(request, 'Bad Credentials')

    return render(request, 'login.html', {})


def register(request):
    if request.POST:
        user_dto = request_to_dto(request)
        user = to_user_model(user_dto)
        employee = to_employee_model(user_dto)
        user.save()
        employee.auth_user = user
        employee.profile_picture = save_file(request.FILES['file'])
        send_verification_token(user=user, template_name='verifiction.html', subject='Activation Link')
        employee.save()
        return render(request, 'reg_successful.html', {'user_name': user.username})
    return render(request, 'registration.html', {})


@login_required
def sign_out(request):
    logout(request)
    redirect_url = reverse_lazy('main')
    return redirect(redirect_url)
