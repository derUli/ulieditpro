#!/usr/bin/python
# -*- coding: utf8 -*-



import os
import shutil

import sys


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
      print("You ha've to install following python-modules manually:")
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
      shutil.copytree("src/", "/opt/ulieditpro")
      print("Finish")
   except IOError, e:
      print(str(e))
      sys.exit(777)
   except OSError, e:
      print(str(e))
      sys.exit(777) 