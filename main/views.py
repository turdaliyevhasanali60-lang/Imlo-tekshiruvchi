from django.shortcuts import render
from .models import *

def index(request):
    correct = None
    incorrects = None
    message = None
    search = request.GET.get('search')
    if search:
        search = search.lower()
        corrects = Correct.objects.filter(word=search)
        if corrects.exists():
            correct = corrects.first()
            incorrects = Incorrect.objects.filter(correct=correct)
        else:
            incorrects = Incorrect.objects.filter(word=search)
            if incorrects.exists():
                incorrect = incorrects.first()
                correct = incorrect.correct
                incorrects = correct.incorrect_set.all()
            else:
                if "x" not in search and "h" not in search:
                    message = "The word doesn't contain either 'h' or 'x'"
                else:
                    message = "The word doesn't exist"

    context = {
        'search': search,
        'correct': correct,
        'incorrects': incorrects,
        'message': message
    }

    return render(request, 'index.html', context)