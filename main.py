#!/usr/bin/python
# -*- coding: utf8 -*-
import uliedit_gui
import wx
import os
import sys
import codecs

class Main:

    def __init__(self):
        self.app = wx.App()
        self.fs_enc = sys.getfilesystemencoding()
        self.initializeSettings()
        self.mainFrame = uliedit_gui.MainFrame(None)
        self.mainFrame.Show(True)
        self.bindEvents()
        self.app.MainLoop()



    def initializeSettings(self):
        self.home_dir = os.path.expanduser("~")
        self.settings_dir = os.path.join(self.home_dir,
                                         ".uliedit")
        self.last_path_file = os.path.join(self.settings_dir, "last_path")
        
        if not os.path.exists(self.settings_dir):
            os.makedirs(self.settings_dir, 0777)

        if os.path.exists(self.last_path_file):
            handle = open(self.last_path_file, "rb")
            self.last_path = handle.read()
            handle.close()
        else:
            handle = open(self.last_path_file, "wb")
            handle.write(self.home_dir)
            handle.close()

        if not os.path.exists(self.last_path):
            self.last_path = self.home_dir

            

        
        

    def onQuit(self, evt):
        # hier muss dann geprüft werden, ob offene Dateien modifiziert wurden
        # gegebenfalls nachfragen, ob er speichern soll
        self.askForSaveOnQuit()



    def askForSaveOnQuit(self):
         sys.exit(0)
        



    def onRibbonTabChange(self, evt):
        self.mainFrame.Refresh()
        evt.Skip()


    def bindEvents(self):

        # Shutdown Events
        self.app.Bind(wx.EVT_QUERY_END_SESSION,
                      self.onQuit)
        self.app.Bind(wx.EVT_END_SESSION,
                 self.onQuit)
        
        self.mainFrame.Bind(wx.EVT_CLOSE,
                 self.onQuit)

        self.mainFrame.ribbons.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.onRibbonTabChange)


if __name__ == '__main__':
    Main()
