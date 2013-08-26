#!/usr/bin/python
# -*- coding: utf8 -*-



import os
import shutil

import sys




INSTALL_SRC = "src/"
INSTALL_TARGET = "/opt/ulieditpro"
ICON_PATH = "/usr/share/applications"

SYMLINK1 = "/usr/bin/ulieditpro"
SYMLINK2 = "/usr/bin/uliedit"

START_SCRIPT = INSTALL_TARGET + "/ulieditpro.sh"

def deleteExistingFiles():
      print("Deleting existing files ...")
      os.system("rm -rf " + SYMLINK1 )
      os.system("rm -rf " + SYMLINK2 )
      os.system("rm -rf " + ICON_PATH + "/uliedit-pro.desktop")
      os.system("rm -rf " + INSTALL_TARGET)
      os.system("rm -f /usr/share/man/de/man1/ulieditpro.1")
      os.system("rm -f /usr/share/man/de/man1/uliedit.1")
      print("Finished...")




print("UliEdit Pro Setup")
print("")
if "uninstall" in sys.argv:
   deleteExistingFiles()
   sys.exit()

print("Do you wan't do install the dependencies?")

try:
   yes_no = raw_input("yes or no? [yes] ").strip()
except KeyboardInterrupt:
   print("")
   sys.exit(666)


if yes_no == 'yes' or yes_no == "":
   print("Please select your package system:")
   print("1 DEB")
   print("2 RPM")
   print("3 Other")
   try:
       pkg_system = raw_input("Package System [1] ").strip()
   except KeyboardInterrupt:
      print("")
      sys.exit(666)

   if pkg_system == '':
      pkg_system = '1'
   if pkg_system == '1':
      os.system("apt-get install python-wxgtk2.8")
   elif pkg_system == '2':
      os.system("yum install wxPython")
   else:
      print("You have to install following python-modules manually:")
      print("wxPython")






print("Install UliEdit Pro to " + INSTALL_TARGET + "yes or no [yes]")

try:
   yes_no = raw_input("yes or no? [yes] ").strip()
except KeyboardInterrupt:
   print("")
   sys.exit(666)


if yes_no == 'yes' or yes_no == "":
   try:
      deleteExistingFiles()
      

      
      if os.path.exists(ICON_PATH):
              print("Create starter Icon...")
              shutil.copyfile(INSTALL_SRC + "ulieditpro.desktop", ICON_PATH + "/uliedit-pro.desktop")
      else:

            print("")
            print("Warning: Can't find " + ICON_PATH)
            print("Note: If you want a starter for this Application on your Desktop, you have to create it by yourself")
            print("Note: If you want a starter for this Application on your Desktop, you have to create it by yourself")
      print("Finish")

      sys.exit(0)
   except IOError, e:
      print(str(e))
      sys.exit(777)
   except OSError, e:
      print(str(e))
      sys.exit(777) 
