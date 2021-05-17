import platform
import os

if platform.system() == "Windows":
    base_path = "C:\\Users\\Yu\\Desktop\\videos"
elif platform.system() == "Linux":
    base_path = "/disk2/11811811/videos"


def get_path(task_id) -> str:
    if platform.system() == "Windows":
        return base_path + "\\" + task_id + "\\" + "video.mp4"
    elif platform.system() == "Linux":
        return base_path + "/" + task_id + "/" + "video.mp4"


def mkdir(task_id):
    if platform.system() == "Windows":
        path = base_path + "\\" + task_id
    elif platform.system() == "Linux":
        path = base_path + "/" + task_id

    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
