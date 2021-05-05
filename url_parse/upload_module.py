from django.http import HttpResponse
import json
from . import models


def upload_task_function(request):
    print(request.FILES)
    if request.method == "POST":
        task_id = request.GET.get('task_id')
        result = models.TASK.objects.get(TASK_ID=task_id)
        if result is not None:
            result.STATUS = 'UPLOADED'
            result.save()
            video = request.FILES['file']
            path = result.FILE_PATH
            file_writer = open(path,'wb+')
            for chunk in video.chunks():
                file_writer.write(chunk)
            file_writer.close()

            data = {
                'success': 'success',
                'task_id': result.TASK_ID,
                'status': result.STATUS,
                'file_path': result.FILE_PATH
            }

            return HttpResponse(json.dumps(data), content_type='application/json')
    data = {
        'success' : 'failed',
        'task_id' : None,
        'status' : None,
        'file_path': None
    }

    return HttpResponse('bad')



