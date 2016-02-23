from restclients.models.panopto import RemoteRecorder, Device
from restclients.panopto import get_resource


def get_remote_recorder_by_id(remote_recorder_id):
    url = "/Panopto/Api/remoteRecorders/%s" % remote_recorder_id

    data = get_resource(url)

    for entry in data.get('Devices', []):
        device = _device_from_json(entry)
        device.remote_recorder_id = data['Id']
        device.save()

    return _remote_recorder_from_json(data)


def get_remote_recorders():
    url = "/Panopto/Api/remoteRecorders/"

    data = get_resource(url)

    remote_recorders = []
    for datum in data:
        for entry in datum.get('Devices', []):
            device = _device_from_json(entry)
            device.remote_recorder_id = datum['Id']
            device.save()

        remote_recorders.append(_remote_recorder_from_json(datum))

    return remote_recorders


def _remote_recorder_from_json(data):
    remote_recorder = RemoteRecorder()
    remote_recorder.id = data['Id']
    remote_recorder.name = data['Name']
    remote_recorder.primary_audio_device_id = data['PrimaryAudioDeviceId']
    remote_recorder.primary_video_device_id = data['PrimaryVideoDeviceId']

    return remote_recorder


def _device_from_json(data):
    device = Device()
    device.id = data['DeviceId']
    device.name = data['Name']
    device.audio_preview_url = data['AudioPreviewUrl']
    device.video_preview_url = data['VideoPreviewUrl']

    return device
