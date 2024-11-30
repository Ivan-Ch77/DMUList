from django.shortcuts import render, get_object_or_404
from .models import Project
from django.http import Http404


def project_list(request):
    projects = Project.objects.all()
    return render(request,
                  'project_list/project/list.html',
                  {'projects': projects})


def project_detail(request, id):
    project = get_object_or_404(Project,
                                id=id)
    return render(request,
                  'project_list/project/detail.html',
                  {'project': project})
