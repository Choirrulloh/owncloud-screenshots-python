import os.path.join

# OwnCloud configuration
OWNCLOUD_DOMAIN = "CHANGE ME"       # The address where your OwnCloud is hosted. (e.g. http://example.com/owncloud)
OWNCLOUD_USER_NAME = "CHANGE ME"    # Your OwnCloud user name.
OWNCLOUD_PASSWORD = "CHANGE ME"     # Your OwnCloud password

OWNCLOUD_DIR = "screenshots"        # The name of the directory in OwnCloud where your
                                    # screenshots will be hosted.

# Bit.ly configuration
BITLY_ACCESS_TOKEN = "CHANGE ME"    # You can get an access token in your bit.ly preferences.
BITLY_DOMAIN = "j.mp"               # A domain supported by Bitly. (e.g. "bit.ly" or "j.mp")

# Local configuration
SCREENSHOTS_FOLDER = os.path.join(os.path.expanduser('~'), 'Desktop') 
                                    # Screenshots folder. Default: desktop.
