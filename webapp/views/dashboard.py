from django.shortcuts import render


def dashboard(request, template_name='webapp/home.html'):
    context = dict()
    return render(request, template_name, context)
