from django.shortcuts import render
from django.http import HttpResponse
from bank_system.models import *
from rest_framework import viewsets
from bank_system.serializer import AccountSerializer


def index(request):
    return HttpResponse("Hello world. you're at the bank system index.")


def to_login_view(request):
    return render(request, 'login.html')


def login_view(request):
    acc_no = request.POST.get('acc_no', '')
    pin = request.POST.get('pin', '')

    if acc_no and pin:
        c = Account.objects.filter(acc_no=acc_no, pin=pin).count()
        if c >= 1:
            return HttpResponse('successful')
        else:
            return HttpResponse('wrong acc')

    else:
        return HttpResponse('Ops')


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer