from django.shortcuts import render
from django.http import JsonResponse
from .gmail import Atro
# Create your views here.
def checker(request,email):
    return JsonResponse(Atro.GmailChecker(email).__str__())
