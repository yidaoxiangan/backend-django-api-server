from django.http import FileResponse
from . import models

def download_task_function(request):

    if request.method == 'GET':
        task_id = request.GET.get('task_id')
        result = models.TASK.objects.get(TASK_ID=task_id)
        if result.STATUS == 'UPLOADED':
            video_path = result.FILE_PATH
            print(video_path)
            video = open(video_path,'rb')
            return FileResponse(video, content_type='video/mp4')





