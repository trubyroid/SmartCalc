from setuptools import setup

APP_NAME = 'SmartCalc_v3'
APP = ['main.py']
DATA_FILES = ['history.pickle']

OPTIONS = {
    'iconfile': 'calc_icon.icns',
    'argv_emulation': False,
    'plist': {
        'CFBundleShortVersionString': '3.0',
        'CFBundleName': 'SmartCalc',
    }
}

setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)
