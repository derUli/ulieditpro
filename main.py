#!/usr/bin/python
# -*- coding: utf8 -*-
import uliedit_gui
import wx
import os
import sys
import codecs
import shutil
import uliedit_charset_helper

class Main:

    def __init__(self):
        self.app = wx.App()
        self.fs_enc = sys.getfilesystemencoding()
        self.initializeSettings()
        self.mainFrame = uliedit_gui.MainFrame(None)
        self.initFields()
        self.icon = wx.Icon(U"images/icon.ico", wx.BITMAP_TYPE_ICO)
        self.mainFrame.SetIcon(self.icon)
        self.mainFrame.Show(True)
        self.bindEvents()
        self.app.MainLoop()

    def onOpenFileDialog(self, evt):
        self.openFileDialog()






    def saveLastPath(self , path):
            # Save Last Path
            handle = open(self.last_path_file, "wb")
            handle.write(unicode(path))
            handle.close()
            self.last_path = path

    def openFileDialog(self):
        dialog = wx.FileDialog(parent = self.mainFrame,
                               message = "Open File",
                               defaultDir = self.last_path,
                               style = wx.OPEN)

        if dialog.ShowModal() == wx.ID_OK:
            self.last_path = dialog.GetPath()
            self.last_path = os.path.dirname(self.last_path)

            self.saveLastPath(self.last_path)
            self.openFile(dialog.GetPath())

    def openFile(self, filename):
        encoding = uliedit_charset_helper.detect_encoding(filename)
        if encoding:
            wx.MessageDialog(None,
                        encoding, "Encoding of " + os.path.basename(filename),
                        wx.OK | wx.ICON_INFORMATION).ShowModal()
            





    def setTitle(self, filename):
        self.mainFrame.SetTitle("UliEdit Pro - " + filename)


        


    def initFields(self):
        chSyntaxHighlighting = self.mainFrame.chSyntaxHighlighting
        chSyntaxHighlighting.Clear()
        chSyntaxHighlighting.Append("ADA")
        chSyntaxHighlighting.Append("ASP")
        chSyntaxHighlighting.Append("AVE")
        chSyntaxHighlighting.Append("BAAN")
        chSyntaxHighlighting.Append("BATCH")
        chSyntaxHighlighting.Append("BULLANT")
        chSyntaxHighlighting.Append("CONF")
        chSyntaxHighlighting.Append("C++")
        chSyntaxHighlighting.Append("DIFF")
        chSyntaxHighlighting.Append("EIFFEL")
        chSyntaxHighlighting.Append("EIFFELKW")
        chSyntaxHighlighting.Append("ERRORLIST")
        chSyntaxHighlighting.Append("HTML")
        chSyntaxHighlighting.Append("LATEX")
        chSyntaxHighlighting.Append("LISP")
        chSyntaxHighlighting.Append("LUA")
        chSyntaxHighlighting.Append("MAKEFILE")
        chSyntaxHighlighting.Append("MATLAB")
        chSyntaxHighlighting.Append("NNCRONTAB")
        chSyntaxHighlighting.Append("PASCAL")
        chSyntaxHighlighting.Append("PLAIN")
        chSyntaxHighlighting.Append("PERL")
        chSyntaxHighlighting.Append("PHP")       
        chSyntaxHighlighting.Append("PROPERTIES")   
        chSyntaxHighlighting.Append("PYTHON")    
        chSyntaxHighlighting.Append("RUBY")   
        chSyntaxHighlighting.Append("SQL")   
        chSyntaxHighlighting.Append("TCL")  
        chSyntaxHighlighting.Append("VB")  
        chSyntaxHighlighting.Append("VBSCRIPT")  
        chSyntaxHighlighting.Append("XML")
        chSyntaxHighlighting.SetSelection(20)


        chbWrapLines = self.mainFrame.chbWrapLines

        chbWrapLines.SetValue(True)


        self.setTitle("untitled")

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
            self.last_path = self.home_dir

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

        self.mainFrame.btnOpen.Bind(wx.EVT_BUTTON,
                                             self.onOpenFileDialog)


if __name__ == '__main__':
    Main()
