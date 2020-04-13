Introduction
------------

This module will publish/update an Android apk programmatically (dynamically), from an Android project, faster and without Android Studio, to the Google Play Store.

## Installation

Install via pip:

    pip install os_android_apk_google_play_publisher

## Quick Usage       
From Python:
    
    import os_android_apk_google_play_publisher.apk_publisher as ap
    
    ap.publish_apk('com.my.packagename',
                   '/path/to/my.apk',
                   '/path/to/client_secrets.json',
                   '0.5',   # publish percent
                   '3')     # version code

If you want to update an already uploaded rollout, set None in the apk path argument in the publish_apk function.   

## Client Secrets
To use the Google Play Console API you would need to allow it from your Play Console account. Then you could download the client_secrets.json file.
    
So log in to your Play Store developer account -> click on Settings -> API Access -> open the developer api and follow the instructions there to download the client_secrets.json file.
                                                           		 



## Links
If you all about automation, why use Android Studio?:  
[os_android_apk_builder-py](https://github.com/osfunapps/os_android_apk_builder-py) -> Create an Android apk programmatically (dynamically), from an Android project, faster and without Android Studio.    


## Licence
MIT