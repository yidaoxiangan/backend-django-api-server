# API guide

本后端服务总共4个API，分别为创建（create），查询（query），上传（upload），下载（download）

## create
使用这个API来创建一个视频处理任务。

### 使用格式

**GET**方法

```
http://10.20.61.169:8080/create/
```

### 返回值

json格式。

```json
{"success": "success", "task_id": "761735f5fa71c973ea7de6187fdc51258f6100ad"}
```

其中，`success`代表是否成功(这个API一般不会失败)，`task_id`是该任务的唯一id，需要在客户端被记录下来。

## query

使用这个API来查询某个视频处理任务的处理状态。

### 使用方法

GET方法
```
http://10.20.61.169:8080/query/?task_id=761735f5fa71c973ea7de6187fdc51258f6100ad
```

参数`task_id`指定要查询的任务。

### 返回值
json格式。

#### 成功形式
```json
{
  "success": "success",
 "task_id": "761735f5fa71c973ea7de6187fdc51258f6100ad", 
 "status": "CREATED", 
 "address": "/disk2/11811811/videos/761735f5fa71c973ea7de6187fdc51258f6100ad/video.mp4"
}
```

#### 失败形式
例如，指定不存在的`task_id`

```
http://10.20.61.169:8080/query/?task_id=34959543
```

```json
{"success": "fail", "task_id": null, "status": null, "address": null}
```

## upload

使用这个方法来向一个创建好的任务上传视频。

### 使用方法

POST方法

```
http://10.20.61.169:8080/query/?task_id=761735f5fa71c973ea7de6187fdc51258f6100ad
```

指定POST请求Body类型为`form-data`，同时设置两个key。

1. enctype=multipart/form-data  设置为text类型。
2. file=[target_file_path] 设置为file类型。

一个POST的例子为
```
POST /upload/?task_id=f15edcd1ec4a4df115659e3b26d6c81b3ab0d882 HTTP/1.1
Host: 10.20.61.169:8080
Cache-Control: no-cache
Postman-Token: 8d7f2703-05ca-3363-3444-ef16cb2427d3
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="enctype="

multipart/form-data
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file"; filename="sample-mp4-file.mp4"
Content-Type: video/mp4


------WebKitFormBoundary7MA4YWxkTrZu0gW--
```

### 返回值

如果未上传过视频并且成功上传，返回值如下

```json
{
    "success": "success",
    "task_id": "761735f5fa71c973ea7de6187fdc51258f6100ad",
    "status": "UPLOADED",
    "file_path": "/disk2/11811811/videos/761735f5fa71c973ea7de6187fdc51258f6100ad/video.mp4"
}
```

如果已经上传过视频（即任务`status`为`UPLOADED` 或是 `FINISHED`)，则上传失败，返回值如下
```json
{
    "success": "failed",
    "task_id": "761735f5fa71c973ea7de6187fdc51258f6100ad",
    "status": "UPLOADED",
    "file_path": "/disk2/11811811/videos/761735f5fa71c973ea7de6187fdc51258f6100ad/video.mp4"
}
```

## download

使用这个API来下载一个已经处理好的视频(只有当视频状态为`FINISHED`时会下载成功)。测试时我设置成了`UPLOADED`时就会下载成功。
(只要上传后就能下载)

### 使用方法

GET方法。
```
http://10.20.61.169:8080/download/?task_id=761735f5fa71c973ea7de6187fdc51258f6100ad
```

### 返回值

直接返回视频，如果无视频，返回404页面。请确认视频上传后（完成处理后）再使用下载API。