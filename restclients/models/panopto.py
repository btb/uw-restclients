from django.db import models


class RemoteRecorder(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    name = models.CharField(max_length=128)
    primary_audio_device = models.ForeignKey('Device')
    primary_video_device = models.ForeignKey('Device')


class Device(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    remote_recorder = models.ForeignKey(RemoteRecorder)
    name = models.CharField(max_length=128)
    audio_preview_url = models.URLField()
    video_preview_url = models.URLField()
