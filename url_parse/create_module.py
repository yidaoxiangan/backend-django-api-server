import hashlib
import json
import time
import random
from . import constant
from . import models

from django.http import HttpResponse

def generate_task_id():

    hash_generator = hashlib.sha1()
    # generate the seed of task id
    seed = str(time.time())
    seed += str(random.randint(1, 100000))

    hash_generator.update(seed.encode('utf-8'))

    task_id = hash_generator.hexdigest()
    # ! check if the task_id has been put in database here
    # ! make sure that the task_id will not override

    return task_id


def create_task_response(request):

    result = 1
    while result is not None:
        try:
            task_id = generate_task_id()
            result = models.TASK.objects.get(TASK_ID=task_id)
        except Exception:
            result = None

    data = {
        'success': 'success',
        'task_id': task_id
    }
    # ip = request.META.get('REMOTE_ADDR')
    # print('Create request from ', str(ip), " url is ", str(request.path))

    task_record = models.TASK()
    task_record.TASK_ID = task_id
    task_record.STATUS = "CREATED"
    task_record.FILE_PATH = constant.base_path + "\\" + task_id + ".mp4"
    task_record.save()

    response = HttpResponse(json.dumps(data), content_type='application/json')
    return response
