from os import path
import re

from pyaapt.utils import popen3
from pyaapt.apk_info import ApkInfo


def get_apk_info(filename):
    AAPT_CMD = 'aapt dump badging %s'
    if not path.exists(filename) or not path.isfile(filename):
        raise Exception('File not found.')

    cmd = AAPT_CMD % filename
    stdin, stdout, stderr, proc = popen3(cmd)
    stderr_data = stderr.read()
    if len(stderr_data) > 0:
        raise Exception('Something goes wrong while reading the Android APK file.')

    data = stdout.read()

    match = re.search(
        r"package: name='([\w|\d|\.]+)' versionCode='(\d+)' versionName='([\w|\d|\.]+)'",
        data
    )
    package_name = match.group(1)
    version_code = match.group(2)
    version_name = match.group(3)

    match = re.search(r"sdkVersion:'(\d+)'", data)
    version_sdk = match.group(1)

    match = re.search(r"targetSdkVersion:'(\d+)'", data)
    version_target_sdk = match.group(1)

    uses_permission = re.findall(
        r"uses-permission: name='(.+)'",
        data
    )
    application_label = dict(re.findall(r"application-label-(.+):'(.+)'", data))
    application_icon = dict(re.findall(r"application-icon-(.+):'(.+)'", data))

    return ApkInfo(package_name, version_code, version_name,
                 version_sdk, version_target_sdk, uses_permission,
                 application_label, application_icon)