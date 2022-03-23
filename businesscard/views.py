from django.shortcuts import render


def businesscard(request):

    return render(
        request,
        'businesscard/business_card.html'
    )