from django.http import FileResponse
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from . import models


def download_task_function(request):
    if request.method == 'GET':
        task_id = request.GET.get('task_id')
        try:
            result = models.TASK.objects.get(TASK_ID=task_id)
        except ObjectDoesNotExist:
            result = None

        if result is not None and result.STATUS == 'UPLOADED':
            video_path = result.FILE_PATH
            print(video_path)
            video = open(video_path, 'rb')
            return FileResponse(video, content_type='video/mp4')
        else:
            return HttpResponseNotFound()

    else:
        return HttpResponseNotAllowed("POST")
