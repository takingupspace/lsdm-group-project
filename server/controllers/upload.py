from pytube import YouTube
import subprocess
import os
import boto3
import pathlib
import shutil
import sys


def DownloadYT(url):
    YouTube(url).streams.get_highest_resolution().download()
    yt = YouTube(url)
    #file_path = '\''
    file_path = yt.title
    file_path += '.mp4'
    #file_path += '\''
    print(file_path)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
    s3 = boto3.client("s3")
    bucket_name = "cloud-computing-gp"
    object_name = file_path
    source = '/var/www/html/pythoncloud/' + file_path
    target = '/var/www/html/pythoncloud/tempfile'
    shutil.copy(source, target)
    file_name = os.path.join(pathlib.Path(__file__).parent.resolve(), file_path)
    response = s3.upload_file(file_name, bucket_name, object_name)
    return file_path


print(DownloadYT(sys.argv[1]))