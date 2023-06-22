from setuptools import setup

APP_NAME = 'SmartCalc_v3'
APP = ['main.py']
DATA_FILES = ['history.pickle', 'view', 'presenter', 'model']

# OPTIONS = {
#     'iconfile': 'icon.icns',
#     'argv_emulation': True,
#     'includes': ('tkinter', 'matplotlib', 'matplotlib.pyplot', 'tkinter.messagebox',  'numpy', 'math', 'pickle', 'typing'),
#     # 'plist': {
#     #     'CFBundleShortVersionString': '3.0',  # Версия вашего приложения
#     #     'CFBundleName': 'SmartCalc',  # Имя вашего приложения
#     # },
#     'packages': ["tkinter", "matplotlib", "numpy"]
# }

setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    # options={'py2app': OPTIONS},
    setup_requires=['py2exe'],
    # setup_requires=['py2app'],
)
