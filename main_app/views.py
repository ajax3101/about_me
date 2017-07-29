import datetime
import os

from django.shortcuts import render

# Create your views here.
from main_app.models import Skills, Edu


def main(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    title = 'Обо мне'
    dict = {'name': 'Денис Морозов',
            'birthday': datetime.date(1977, 1, 31),
            'tel': '+(380)50-484-72-71',
            'email': 'ajax3101@gmail.com',
            'linkedin': 'https://www.linkedin.com/in/ajax3101/',
            }
    print("BASEDIR = " + BASE_DIR)
    return render(request, 'index.html', dict)


def edu(request):
    records = Edu.objects.all()
    context = dict(records=records)
    return render(request, 'edu.html', context)


def work(request):
    records = Skills.objects.all()
    context = dict(records=records)
    return render(request, 'work.html', context)

# def work(request):
#     records_q = Qualities.objects.all()
#     context_q = dict(records_q=records_q)
#     return render(request, 'work.html', context_q)
