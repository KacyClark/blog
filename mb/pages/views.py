from django.http import HttpResponse
from django.shortcuts import render


def home_view():
    return
        HttpResponse("<h1>Welcome to the Message Board</h1>")