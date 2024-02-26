from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . import models


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'users_count': models.get_user_model().objects.count(),
        'plans_count': models.Plan.objects.count(),
        'tasks_count': models.Task.objects.count(),
    }
    return render(request, 'tasks/index.html', context)
