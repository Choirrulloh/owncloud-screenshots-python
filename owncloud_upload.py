import config, owncloud
from os import path
from shorten import shorten

def upload_and_share(file_path):
    oc = login()

    destination = config.OWNCLOUD_DIR + "/" + get_filename(file_path)

    try:
        # Try to upload file.
        oc.put_file(destination, file_path)
    except owncloud.ResponseError as inst:
        # If it fails because the directory does not yet exist,
        # create the directory and try to upload again.
        if 'HTTP error: 404' in inst.args:
            oc.mkdir(config.OWNCLOUD_DIR)
            oc.put_file(destination, file_path)
        else:
            raise

    # Share file.
    link_info = oc.share_file_with_link(destination)

    # Return shortened.
    return shorten(link_info.link)

def login():
    oc = owncloud.Client(config.OWNCLOUD_DOMAIN)
    oc.login(config.OWNCLOUD_USER_NAME, config.OWNCLOUD_PASSWORD)
    return oc

def get_filename(file_path):
    return path.split(file_path)[-1]