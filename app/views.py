from django.core.mail import send_mail
from django.shortcuts import render, redirect

from portfolio import settings
from .models import *


# def feedback(request):
#     if request.method == "POST":
#         msg = request.POST.get('msg')
#         print(msg)
#         project = request.POST.get('project')
#         print(project)
#         email = request.POST.get('email')
#         # if email:
#         #     msg += f'\nОтправитель: {email}'
#         mail = send_mail(
#             'Фитбэк с сайта-визитки',
#             # msg + project + email,
#             msg,
#             settings.EMAIL_HOST_USER,
#             ['KurochkinAlexei@yandex.ru',],
#             # fail_silently=False
#         )
#     return redirect('index')


def index(request):
    if request.method == "POST":
        msg = request.POST.get('msg')
        project = request.POST.get('project')
        email = request.POST.get('email')
        if email:
            msg += f'\nОтправитель: {email}'
        send_mail(
            f'Фитбэк на проект {project}',
            # f'Сообщение: {msg} \nОтправитель: {email}',
            msg,
            settings.EMAIL_HOST_USER,
            ['KurochkinAlexei@yandex.ru'],
            fail_silently=False
        )

    # if request.method == "GET":
    skills = Skill.objects.all()

    for s in skills:
        if s.type == 'progress_bar':
            if s.skill_score > 83:
                s.background = '#A9D18E'
                s.text_on_bar = 'очень хороший'
            elif s.skill_score >= 66:
                s.background = '#C5E0B4'
                s.text_on_bar = 'хороший'
            elif s.skill_score >= 50:
                s.background = '#E2F0D9'
                s.text_on_bar = 'средний'
            else:
                s.background = '#E2F0D9'
                s.text_on_bar = 'начальный'

    projects = Project.objects.all()

    return render(request, 'index.html', {'skills': skills, 'projects': projects})


def test(request):
    return render(request, 'test.html')
