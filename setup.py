from distutils.core import setup

setup(
    name='os_android_apk_google_play_publisher',
    packages=['os_android_apk_google_play_publisher'],
    version='1.04',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='This module will publish an apk programmatically (dynamically), without Android Studio, to Google\'s Play Store, with a specific percent.',  # Give a short description about your library
    author='Oz Shabat',  # Type in your name
    author_email='osfunapps@gmail.com',  # Type in your E-Mail
    url='https://github.com/osfunapps/os_android_apk_google_play_publisher',  # Provide either the link to your github or to your website
    keywords=['python', 'osfunapps', 'apk', 'android', 'automation', 'release', 'publish', 'assemble-release', 'create', 'google-play'],  # Keywords that define your package best
    install_requires=['google-api-python-client', 'oauth2client'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package

        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',  # Again, pick a license

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

