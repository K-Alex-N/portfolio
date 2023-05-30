from django.shortcuts import render
from .models import *

skills = [
    {'name': 'Python', 'value': 90},
    {'name': 'ООП', 'value': 80},
    {'name': 'SQL (PostgreSQL, MySQL)', 'value': 70},
    {'name': 'SQLAlchemy', 'value': 70},
    {'name': 'Django', 'value': 70},
    {'name': 'Flask', 'value': 70},
    {'name': 'Aiohttp', 'value': 50},
    {'name': 'FastAPI', 'value': 50},
    {'name': 'Pytest, Unittest', 'value': 70},
    {'name': 'Алгоритмы и структуры данных', 'value': 90},
    {'name': 'Регулярные выражения', 'value': 70},
    {'name': 'Beautifulsoup, Selenium', 'value': 70},
]


def index(request):
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
