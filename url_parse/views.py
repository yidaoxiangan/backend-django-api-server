from django.http import HttpResponse
from . import create_module
from . import query_module
from . import upload_module


def create_function(request):
    return create_module.create_task_response(request)


def upload_function(request):
    return upload_module.upload_task_function(request)
    return HttpResponse()


def download_function(request):
    return HttpResponse()


def query_function(request):
    return query_module.query_task_response(request)
