from django.http import HttpResponse
import json
from . import models

'''
query format:
    task_id = ""
    
return format:
    success = success / fail
    task_id = task_id
    status = CREATED / UPLOADED / FINISHED
    address = address / null
'''


def query_task_response(request):

    try:
        if request.method == 'GET':
            task_id = request.GET.get('task_id')
            print(task_id)
            result = models.TASK.objects.get(TASK_ID=task_id)
    except Exception:
        result = None

    if result is None:
        data = {
            'success': 'fail',
            'task_id': None,
            'status': None,
            'address': None
        }
    else:
        data = {
            'success': 'success',
            'task_id': result.TASK_ID,
            'status': result.STATUS,
            'address': result.ADDRESS
        }

    return HttpResponse(json.dumps(data), content_type='application/json')
