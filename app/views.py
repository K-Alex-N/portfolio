from django.shortcuts import render

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

    for s in skills:
        if s['value'] > 83:
            s['background'] = '#A9D18E'
            s['text'] = 'очень хороший'
        elif s['value'] >= 66:
            s['background'] = '#C5E0B4'
            s['text'] = 'хороший'
        elif s['value'] >= 50:
            s['background'] = '#E2F0D9'
            s['text'] = 'средний'
        else:
            s['background'] = '#E2F0D9'
            s['text'] = 'начальный'

    return render(request, 'index.html', {'skills': skills})

def test(request):
    return render(request, 'test.html')