import datetime

from django.shortcuts import render


def monday(request):

    now = datetime.datetime.now()

    if now.weekday == 0:
        is_it_monday = True
    else:
        is_it_monday = False

    return render(
        request,
        'monday/monday.html',
        context={
            'is_it_monday': is_it_monday,
        }
    )
