from distutils.core import setup

setup(name='oc_screenshots',
      version='0.9',
      description='OwnCloud Auto Screenshots Uploader',
      author='Simon Slangen',
      requires=['pyocclient', 'pyperclip', 'pync', 'watchdog'],
      )