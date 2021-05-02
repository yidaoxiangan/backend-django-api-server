from django.http import HttpResponse
import json
from . import models


def upload_task_function(request):
    print(request.FILES)
    if request.method == "POST":
        task_id = request.GET.get('task_id')
        result = models.TASK.objects.get(TASK_ID=task_id)
        if result is not None:
            video = request.FILES['file']
            path = result.FILE_PATH
            print(3)
            file_writer = open(path,'wb+')
            for chunk in video.chunks():
                file_writer.write(chunk)
            file_writer.close()

            return HttpResponse('OK')
    return HttpResponse('bad')



