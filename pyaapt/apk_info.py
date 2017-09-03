class ApkInfo(object):
    def __init__(self, package_name, version_code, version_name,
                 version_sdk, version_target_sdk, uses_permission,
                 application_label, application_icon):
        self.package_name = package_name
        self.version_code = version_code
        self.version_name = version_name
        self.version_sdk = version_sdk
        self.version_target_sdk = version_target_sdk
        self.uses_permission = uses_permission
        self.application_label = application_label
        self.application_icon = application_icon