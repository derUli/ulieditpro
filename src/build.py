import sys

from distutils.core import setup
import py2exe
import shutil
import os

shutil.rmtree("dist")

os.mkdir("dist")

shutil.copytree("images", "dist/images")
shutil.copyfile("manpage.html", "dist/manpage.html")

sys.argv.append("py2exe")

setup(options = {
        "py2exe": {
            "dll_excludes": ["MSVCP90.dll"],
            "bundle_files":3
        }
    },
    windows = [
        {
            "script": "main.py",
            "icon_resources": [(0, "images/icon.ico")]
            
        }
    ], zipfile=None
) 

os.rename("dist/main.exe", "dist/uliedit.exe")

shutil.move("dist", "../windows/dist")
