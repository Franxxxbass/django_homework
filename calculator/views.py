from django.shortcuts import render, HttpResponse


def add(request, first_num, second_num):
    result = first_num + second_num
    return render(
        request,
        'calculator/add.html',
        context={
            'first_num': first_num,
            'second_num': second_num,
            'result': result,
        }
    )


def subtract(request, first_num, second_num):
    result = first_num - second_num
    return render(
        request,
        'calculator/subtract.html',
        context={
            'first_num': first_num,
            'second_num': second_num,
            'result': result,
        }
    )


def multiply(request, first_num, second_num):
    result = first_num * second_num
    return render(
        request,
        'calculator/multiply.html',
        context={
            'first_num': first_num,
            'second_num': second_num,
            'result': result,
        }
    )


def divide(request, first_num, second_num):

    result = first_num / second_num
    return render(
        request,
        'calculator/divide.html',
        context={
            'first_num': first_num,
            'second_num': second_num,
            'result': result,
            }
        )


