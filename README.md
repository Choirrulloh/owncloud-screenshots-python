# owncloud-screenshots-python
Limited to **Mac OS X** at the moment.

Auto-uploads screenshots to your OwnCloud host and copies the link to your clipboard. Written in Python.

## Dependencies
No install script yet, so you need to manually install the required packages on your system.
* pyocclient (Python client library for OwnCloud)
* pyperclip (A cross-platform clipboard module for Python)
* pync (Mac OS X notifications)
* watchdog (To monitor file/folder changes)

e.g. to install using pip:

`pip install pyocclient pyperclip pync watchdog`

## Usage
You'll need an existing OwnCloud installation and a Bitly account.

* Add your OwnCloud credentials and Bitly access token to `config.py`
* Run `screenshot_watcher.py` in the background.
 * e.g. in Terminal: `python screenshot_watcher.py &`
* Enjoy.
