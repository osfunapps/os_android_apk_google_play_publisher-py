import os_android_apk_google_play_publisher.modules.apk_publisher_boilerplate as bp


################################################################################
#
# This module meant to upload a new apk release to the Play Store.
#
# Make sure you have the client-secrets.json file. If you don't have it,
# read in the GitHub repo on how to acquire it:
# https://github.com/osfunapps/os_android_apk_google_play_publisher
#
################################################################################


def publish_apk(package_name, apk_file_path, client_secrets_path, publish_percent, version_code):
    """
    Will publish a new apk to the Google's Play Store (you HAVE to have a published app in the Google's Play Store already)
    Args:
        param package_name: your app's package name
        param apk_file_path: the path to your apk file
        param client_secrets_path: the path to your Google's client secrets json (read on how to obtain at 'os_android_apk_google_play_publisher <https://github.com/osfunapps/os_android_apk_google_play_publisher>')
        param publish_percent: roll out percents are -> 0.1 to 10%, 0.85 to 85% etc...
        param version_code: the version code of the current apk
    """

    # Declare command-line flags.
    parsed_flags = bp.parse_flags()

    upload = 'false'
    if apk_file_path is not None:
        upload = 'true'

    bp.publish_apk(parsed_flags, package_name, apk_file_path, publish_percent, version_code, client_secrets_path, upload)
