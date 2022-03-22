from django.shortcuts import render


def add(request, first_num, second_num):

    result = first_num + second_num
    return render(
        request,
        'calculator/add.html',
        context = {
            'first_num': first_num,
            'second_num': second_num,
            'result': result,
        }
    )

def substract(request, first_num, second_num):

    result = first_num - second_num
    return render(
        request,
        'calculator/substract.html',
        context = {
            'first_num': first_num,
            'second_num': second_num,
            'result': result,
        }
    )