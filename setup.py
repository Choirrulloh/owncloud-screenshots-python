from distutils.core import setup

setup(name='owncloud-screenshots-python',
      version='0.9',
      description='OwnCloud Auto Screenshots Uploader',
      author='Simon Slangen',
      requires=['pyocclient', 'pyperclip', 'pync', 'watchdog']
      )