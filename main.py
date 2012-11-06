#!/usr/bin/python
# -*- coding: utf8 -*-
import uliedit_gui
import wx
import sys

class Main:

    def __init__(self):
        self.app = wx.App()

        self.mainFrame = uliedit_gui.MainFrame(None)
        self.mainFrame.Show(True)
        self.bindEvents()
        self.app.MainLoop()

        

    def onQuit(self, evt):
        # hier muss dann geprüft werden, ob offene Dateien modifiziert wurden
        # gegebenfalls nachfragen, ob er speichern soll
        self.askForSaveOnQuit()



    def askForSaveOnQuit(self):
         sys.exit(0)
        



    def onRibbonTabChange(self, evt):
        self.mainFrame.ribbons.Refresh()


    def bindEvents(self):

        # Shutdown Events
        self.app.Bind(wx.EVT_QUERY_END_SESSION,
                      self.onQuit)
        self.app.Bind(wx.EVT_END_SESSION,
                 self.onQuit)
        
        self.mainFrame.Bind(wx.EVT_CLOSE,
                 self.onQuit)

        self.mainFrame.ribbons.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.onRibbonTabChange)


if __name__ == '__main__':
    Main()
