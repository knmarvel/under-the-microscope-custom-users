from django.shortcuts import render


def index(request):
    html = "index.html"
    content = "Hi from Kano"
    return render(request, html, {"content": content})