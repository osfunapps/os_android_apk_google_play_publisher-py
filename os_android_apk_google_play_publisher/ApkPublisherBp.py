###########################################################################
#
# just the boiler plate of the apk publisher file
#
###########################################################################
import argparse
from apiclient import sample_tools
from oauth2client import client


def publish_apk(parsed_flags, package_name, apk_file_path, publish_percent, version_code, client_secrets_dir, publish):
    args = [str(__file__), package_name, apk_file_path, str(publish_percent), 'production', str(version_code), publish]

    # Authenticate and construct service.
    service, flags = sample_tools.init(
        args,
        'androidpublisher',
        'v3',
        __doc__,
        client_secrets_dir, parents=[parsed_flags],
        scope='https://www.googleapis.com/auth/androidpublisher')

    # Process flags and read their values.
    package_name = flags.package_name
    apk_file = flags.apk_file
    user_fraction = float(flags.user_fraction)

    track = flags.track
    version_code = float(flags.version_code)
    upload = flags.upload

    try:
        edit_request = service.edits().insert(body={}, packageName=package_name)
        result = edit_request.execute()
        edit_id = result['id']

        if upload == 'true':
            print("uploading...")
            apk_response = service.edits().apks().upload(
                editId=edit_id, packageName=package_name, media_body=apk_file).execute()
            version_code = apk_response['versionCode']
            print('Version code %d has been uploaded' % apk_response['versionCode'])

        track_response = service.edits().tracks().update(
            editId=edit_id,
            track=track,
            packageName=package_name,
            body={u'releases': [obtain_json(user_fraction, version_code)]}).execute()

        print('Track %s is set with releases: %s' % (
            track_response['track'], str(track_response['releases'])))

        commit_request = service.edits().commit(
            editId=edit_id, packageName=package_name).execute()

        print('Edit "%s" has been committed' % (commit_request['id']))

    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run the '
              'application to re-authorize')


def obtain_json(user_fraction, version_code):
    if user_fraction != 1:
        return {
            u'name': u'Automated release',
            u'versionCodes': [version_code],
            u'userFraction': user_fraction,
            u'status': u'inProgress'
        }

    else:
        return {
            u'name': u'Automated release',
            u'versionCodes': [version_code],
            u'status': u'completed'
        }


# will parse the required flags for the roll out
def parse_flags():
    arg_parser = argparse.ArgumentParser(add_help=False)
    arg_parser.add_argument('package_name',
                            help='The package name. Example: com.android.sample')
    arg_parser.add_argument('apk_file',
                            nargs='?',
                            default='apk.apk',
                            help='The path to the APK file to upload.')
    arg_parser.add_argument('user_fraction',
                            nargs='?',
                            default='0.0',
                            help='user percentage')
    arg_parser.add_argument('track',
                            nargs='?',
                            default='0.0',
                            help='should be wither roll out or production')
    arg_parser.add_argument('version_code',
                            nargs='?',
                            default='0.0',
                            help='version code')
    arg_parser.add_argument('upload',
                            nargs='?',
                            default='0.0',
                            help='should upload the apk or not')
    return arg_parser
