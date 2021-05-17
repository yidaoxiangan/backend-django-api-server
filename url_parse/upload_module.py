from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
import json
from . import models


def upload_task_function(request):

    if request.method == "POST":
        task_id = request.GET.get('task_id')
        result = models.TASK.objects.get(TASK_ID=task_id)
        if result is not None:
            if result.STATUS == 'CREATED':
                result.STATUS = 'UPLOADED'
                result.save()
                video = request.FILES['file']
                path = result.FILE_PATH
                file_writer = open(path, 'wb+')
                for chunk in video.chunks():
                    file_writer.write(chunk)
                file_writer.close()

                successful_data = {
                    'success': 'success',
                    'task_id': result.TASK_ID,
                    'status': result.STATUS,
                    'file_path': result.FILE_PATH
                }

                return HttpResponse(json.dumps(successful_data), content_type='application/json')
            else:
                failed_data = {
                    'success': 'failed',
                    'task_id': task_id,
                    'status': result.STATUS,
                    'file_path': result.FILE_PATH
                }
                return HttpResponse(json.dumps(failed_data), content_type='application/json')
    else:
        return HttpResponseNotAllowed("POST")

