import zipfile
import os

##working_folder = '/home/nick/Desktop/textrpg/textrpg'

working_folder = os.getcwd()

files = os.listdir(working_folder)

files_py = []

for f in files:
    if f.endswith('py'):
        fff = os.path.join(working_folder, f)
        files_py.append(fff)

ZipFile = zipfile.ZipFile("textrpg.zip", "w" )

for a in files_py:
    print(a)
    ZipFile.write(os.path.basename(a), compress_type=zipfile.ZIP_DEFLATED)
