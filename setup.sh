#!/usr/bin/python
# -*- coding: utf8 -*-



import os
import shutil

import sys


INSTALL_SRC = "src/"
INSTALL_TARGET = "/opt/ulieditpro"
ICON_PATH = "/usr/local/share/applications"

SYMLINK1 = "/usr/bin/ulieditpro"
SYMLINK2 = "/usr/bin/uliedit"

START_SCRIPT = INSTALL_TARGET + "/ulieditpro.sh"

print("UliEdit Pro Setup")
print("")
print("Do you wan't do install the dependencies?")

try:
   yes_no = raw_input("yes or no? [yes] ").strip()
except KeyboardInterrupt:
   print("")
   sys.exit(666)


if yes_no == 'yes' or yes_no == "":
   print("Please select your package system")
   print("1 DEB")
   print("2 RPM")
   print("3 Not Supported")
   try:
       pkg_system = raw_input("Package System [1] ").strip()
   except KeyBoardInterrupt:
      print("")
      sys.exit(666)
   if pkg_system == '1':
      os.system("apt-get install python-wxgtk2.8")
   elif pkg_system == '2':
      os.system("yum install wxPython")
   else:
      print("You have to install following python-modules manually:")
      print("wxPython")



print("")
print("UliEdit Pro nach /opt/ulieditpro installieren?")

try:
   yes_no = raw_input("yes or no? [yes] ").strip()
except KeyboardInterrupt:
   print("")
   sys.exit(666)


if yes_no == 'yes' or yes_no == "":
   try:

      print("copy files...")
      shutil.copytree(INSTALL_SRC, INSTALL_TARGET)
      print("Finish")
      print("Creating Symlinks...")
      os.symlink(START_SCRIPT, SYMLINK1)
      os.symlink(START_SCRIPT, SYMLINK2)
      print("Finish")
      print("You can start UliEdit Pro by calling one of this commands on shell:")
      print(SYMLINK1)
      print(SYMLINK2)
      
      print("")
      print("Note: If you want a starter for this Application on your Desktop, you have to create it by yourself")
      
      if os.path.exists(ICON_PATH):
              shutil.copyfile(INSTALL_SRC + "/UliEdit Pro.desktop", ICON_PATH + "/UliEdit Pro 1.0.desktop")
      sys.exit(0)
   except IOError, e:
      print(str(e))
      sys.exit(777)
   except OSError, e:
      print(str(e))
      sys.exit(777) 
