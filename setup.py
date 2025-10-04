from cx_Freeze import setup, Executable
import os

path = './asset'
asset_list = os.listdir(path)
asset_complete_path = [os.path.join(path, asset).replace('\\', '/') for asset in asset_list]

executables = [Executable('main.py')]
files = {'include_files': asset_complete_path, 'packages': ['pygame']}

setup(
    name='Mountain Shooter',
    version='1.0',
    description='Mountain Shooter',
    options={'build_exe': {'packages': ['pygame']}},
    executables=executables,
)
