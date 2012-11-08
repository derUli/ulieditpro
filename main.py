#!/usr/bin/python
# -*- coding: utf8 -*-
import uliedit_gui
import wx
import os
import sys
import codecs
import shutil
import uliedit_charset_helper
import uliedit_file_manager
import copy
import lexers

class Main:

    def __init__(self):
        self.app = wx.App()
        self.fs_enc = sys.getfilesystemencoding()
        self.pwd = os.getcwd()
        os.chdir(os.path.dirname(sys.argv[0]))
        self.initializeSettings()
        self.mainFrame = uliedit_gui.MainFrame(None)
        self.initFields()
        self.icon = wx.Icon(U"images/icon.ico", wx.BITMAP_TYPE_ICO)
        self.mainFrame.SetIcon(self.icon)
        
       
        self.file_manager = uliedit_file_manager.UliEditFileManager()
        self.current_file_index = -1
        self.change_lexer(self.current_lexer)        
        self.mainFrame.Show(True)
        self.bindEvents()
        self.parseCommandLineArgs(sys.argv)
        self.app.MainLoop()

    def onOpenFileDialog(self, evt):
        self.openFileDialog()
        self.mainFrame.txtContent.SetFocus()


    def onCopy(self, evt):
        self.mainFrame.txtContent.Copy()
        self.file_manager.setModified(self.current_file_index);
        self.mainFrame.txtContent.SetFocus()


    def onPaste(self, evt):
        self.mainFrame.txtContent.Paste()
        self.file_manager.setModified(self.current_file_index);
        self.mainFrame.txtContent.SetFocus()
        
    def onUndo(self, evt):
        if(self.mainFrame.txtContent.CanUndo()):
           self.mainFrame.txtContent.Undo()
           self.file_manager.setModified(self.current_file_index);
           self.mainFrame.txtContent.SetFocus()


    def onRedo(self, evt):
        if(self.mainFrame.txtContent.CanRedo()):
           self.mainFrame.txtContent.Redo()
           self.file_manager.setModified(self.current_file_index);
           self.mainFrame.txtContent.SetFocus()


    def onChangeText(self ,evt):
        evt.Skip()
        if self.current_file_index > -1:
            try:
                self.file_manager.files[self.current_file_index]["content"] = self.mainFrame.txtContent.GetValue()
            except AttributeError:
                self.file_manager.files[self.current_file_index]["content"] = self.mainFrame.txtContent.GetText()
                self.change_lexer(self.current_lexer)
                self.setTitle
            
            self.file_manager.files[self.current_file_index]["modified"] = True
            


    def onNewFile(self, evt):
        self.openEmptyFile()



    def openEmptyFile(self):
        self.current_file_index = self.file_manager.newFile()
        title = self.file_manager.getFileAtIndex(self.current_file_index)["filename"]
        self.setTitle(title)
        self.mainFrame.cbOpenFiles.Append(title)
        self.mainFrame.cbOpenFiles.SetStringSelection(title)
        self.mainFrame.txtContent.SetFocus()

    def parseCommandLineArgs(self, args):
        if len(args) > 1:
            filename = args[1].decode(self.fs_enc)
            self.openFile(filename)
        else:
           self.openEmptyFile()
            

        

    def saveLastPath(self , path):
            # Save Last Path
            
            self.last_path = unicode(path)
            handle = codecs.open(self.last_path_file,
                                 "wb",
                                 encoding = self.fs_enc)
            handle.write(path)
            handle.close()

    def openFileDialog(self):
        if not os.path.exists(self.last_path):
            self.saveLastPath(self.home_dir)
        
        dialog = wx.FileDialog(parent = self.mainFrame,
                               message = "Open File",
                               defaultDir = self.last_path,
                               style = wx.OPEN | wx.FD_FILE_MUST_EXIST )

        if dialog.ShowModal() == wx.ID_OK:
            self.last_path = dialog.GetPath()
            self.last_path = os.path.dirname(self.last_path)
            self.saveLastPath(self.last_path)
            self.openFile(dialog.GetPath())
            






    def openFile(self, filename):
        filename = os.path.abspath(filename)
        encoding = uliedit_charset_helper.detect_encoding(filename)
        if encoding:
            wx.MessageDialog(None,
                        encoding, "Encoding of " + os.path.basename(filename),
                        wx.OK | wx.ICON_INFORMATION).ShowModal()
                        

            if self.file_manager.isOpen(filename):
                wx.MessageDialog(None,
                        u"This file is already open.",
                                 os.path.basename(filename),
                        wx.OK | wx.ICON_WARNING).ShowModal()
                return False

            else:
                
            
                tmp = self.file_manager.addFile(filename,
                                                encoding)
                line_seperator = self.file_manager.getFileAtIndex(tmp)["line_seperator"]

                self.mainFrame.txtContent.SetEOLMode(line_seperator)
                self.mainFrame.txtContent.ConvertEOLs(line_seperator)
                self.setTitle(os.path.basename(filename))
                if tmp != None:
                    self.current_file_index = copy.copy(tmp)
                    content = self.file_manager.getContentByIndex(self.current_file_index)
                    self.mainFrame.cbOpenFiles.Append(filename)
                    self.mainFrame.cbOpenFiles.SetStringSelection(filename)
                    try:
                        self.mainFrame.txtContent.SetValue(content)
                    except AttributeError:
                        self.mainFrame.txtContent.ClearAll()
                        self.mainFrame.txtContent.SetText(content)
                        self.mainFrame.txtContent.ConvertEOLs(self.file_manager.getFileAtIndex(tmp)["line_seperator"])
                        self.mainFrame.txtContent.SetEOLMode(self.file_manager.getFileAtIndex(tmp)["line_seperator"])
                        self.mainFrame.txtContent.EmptyUndoBuffer()
                        self.mainFrame.txtContent.SetFocusFromKbd()
                        return True                                          
                       
                       
        
                    


                
        else:
            wx.MessageDialog(None,
                        u"Kann das Encoding nicht erkennen!",
                                 os.path.basename(filename),
                        wx.OK | wx.ICON_WARNING).ShowModal()
            return False
            





    def onBtnSave(self, evt):
        self.save_current_file()
        self.mainFrame.txtContent.SetFocus()


    def onBtnSaveAs(self, evt):
        self.openSaveAsDialog()

    def openSaveAsDialog(self):
        if not os.path.exists(self.last_path):
            self.saveLastPath(self.home_dir)
        
        dialog = wx.FileDialog(parent = self.mainFrame,
                               message = "Save As",
                               defaultDir = self.last_path,
                               style = wx.SAVE | wx.FD_OVERWRITE_PROMPT)

        if dialog.ShowModal() == wx.ID_OK:
            self.last_path = dialog.GetPath()
            self.file_manager.getFileAtIndex(self.current_file_index)["filename"] = self.last_path
            self.setTitle(dialog.GetPath())
            self.last_path = os.path.dirname(self.last_path)
            self.saveLastPath(self.last_path)
            return self.save_current_file()
        else:
            return False


            
    def save_file_by_index(self, index):
        tmp_path = self.file_manager.getFileAtIndex(index)["filename"]
        if  tmp_path != None and not tmp_path.startswith("untitled "):
            return self.file_manager.saveFile(index)
        else:
            return self.openSaveAsDialog()


        
    def save_current_file(self):
        tmp_path = self.file_manager.getFileAtIndex(self.current_file_index)["filename"]
        if  tmp_path != None and not tmp_path.startswith("untitled "):
            return self.file_manager.saveFile(self.current_file_index)
        else:
            return self.openSaveAsDialog()



    def setTitle(self, filename):
        self.mainFrame.SetTitle("UliEdit Pro - " + filename)


    def onchbWrapLines(self, evt):
        if self.mainFrame.chbWrapLines.GetValue():

           self.mainFrame.txtContent.SetWrapMode(wx.stc.STC_WRAP_WORD)
           if os.path.exists(self.wrap_words_enabled_file):
              os.unlink(self.wrap_words_enabled_file)
        else:
              self.mainFrame.txtContent.SetWrapMode(wx.stc.STC_WRAP_NONE)   
              open(self.wrap_words_enabled_file, "w").close()      
              

    def onchbDisplayLineEndings(self, evt):
        if self.mainFrame.chbDisplayLineEndings.GetValue():
            open(self.display_line_endings_enabled_file , "w").close()
            self.mainFrame.txtContent.SetViewEOL(True)
        else:
            if os.path.exists(self.display_line_endings_enabled_file):
                os.unlink(self.display_line_endings_enabled_file)
                self.mainFrame.txtContent.SetViewEOL(False)
        
              
               

                   


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
        # Syntax Highlighting voererst deaktiviert,
        # da ich es nicht zum laufen bekomme
        chSyntaxHighlighting.Show(False)
        self.mainFrame.m_staticText1.Show(False)
            
        chbWrapLines = self.mainFrame.chbWrapLines

        font = wx.Font(11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        face = font.GetFaceName()
        size = font.GetPointSize()
        self.mainFrame.txtContent.StyleSetSpec(wx.stc.STC_STYLE_DEFAULT,"face:%s,size:%d" % (face, size))
        
        chbDisplayLineEndings = self.mainFrame.chbDisplayLineEndings

        if not os.path.exists(self.wrap_words_enabled_file):
           self.mainFrame.chbWrapLines.SetValue(True)
        else:
          self.mainFrame.chbWrapLines.SetValue(False)

        if os.path.exists(self.display_line_endings_enabled_file):
            self.mainFrame.txtContent.SetViewEOL(True)
            
            self.mainFrame.chbDisplayLineEndings.SetValue(True)
        else:
            self.mainFrame.txtContent.SetViewEOL(False)
            self.mainFrame.chbDisplayLineEndings.SetValue(False)
            
        
          
        


        self.mainFrame.cbOpenFiles.Clear()
        
        try:
            # Enable line numbers.
            self.mainFrame.txtContent.SetMarginType(1, wx.stc.STC_MARGIN_NUMBER)
            self.mainFrame.txtContent.SetMarginMask(1, 0)
            self.mainFrame.txtContent.SetMarginWidth(1, 25)
            
            # Set Wrap mode default to on
            if not os.path.exists(self.wrap_words_enabled_file):
               self.mainFrame.txtContent.SetWrapMode(wx.stc.STC_WRAP_WORD)
            else:
               self.mainFrame.txtContent.SetWrapMode(wx.stc.STC_WRAP_NONE)
            
        except AttributeError:
            pass
            


        self.setTitle("untitled")

    def initializeSettings(self):
        self.home_dir = os.path.expanduser("~")
        self.settings_dir = os.path.join(self.home_dir,
                                         ".uliedit")
        self.last_path_file = os.path.join(self.settings_dir, "last_path")

        if not os.path.exists(self.settings_dir):
            os.makedirs(self.settings_dir, 0777)


        if os.path.exists(self.last_path_file):
            handle = codecs.open(self.last_path_file, "rb",
                                 encoding = self.fs_enc)
            self.last_path = handle.read()
            handle.close()
        else:
            self.saveLastPath(self.home_dir)
        if not os.path.exists(self.last_path):
            self.last_path = self.home_dir
            
        self.wrap_words_enabled_file = os.path.join(self.settings_dir, "wrap_words_disabled")
        self.display_line_endings_enabled_file = os.path.join(self.settings_dir, "display_line_endings")
        self.current_lexer = "PLAIN"


        
        

    def onQuit(self, evt):
        # hier muss dann geprüft werden, ob offene Dateien modifiziert wurden
        # gegebenfalls nachfragen, ob er speichern soll
        self.askForSaveOnQuit()



    def askForSaveOnQuit(self):
        files = self.file_manager.files
        index = 0
        for file in files:
            if file["modified"]:
                dialog = wx.MessageDialog(self.mainFrame,
                                 "Save this file before quit?",
                                 os.path.basename(file["filename"]),
                                 wx.YES_NO | wx.CANCEL | wx.ICON_WARNING)
                result = dialog.ShowModal()
                if result == wx.ID_CANCEL:
                    return
                elif result == wx.ID_YES:
                    if self.save_file_by_index(index):
                        next
                    else:
                        return
                elif result == wx.ID_NO:
                    next
            index += 1

                            
        os.chdir(self.pwd)
        wx.TheClipboard.Flush()
        sys.exit(0)
        

    def onChangecbOpenFiles(self, evt):
        self.changeCurrentFile(self.mainFrame.cbOpenFiles.GetValue())
        evt.Skip()

    def onchSyntaxHighlightingChange(self, evt):
        lexer_name = self.mainFrame.chSyntaxHighlighting.GetStringSelection()
        self.change_lexer(lexer_name)
        evt.Skip()


    def change_lexer(self, name):
        self.current_lexer = name
        self.mainFrame.txtContent.SetLexer(lexers.getLexer(self.current_lexer))
        #self.mainFrame.txtContent.SetStyleBits(7)




    def changeCurrentFile(self, filename):
        if self.file_manager.isOpen(filename):
            index = self.file_manager.getIndexByFilename(filename)
            content = self.file_manager.getContentByIndex(index)
            
            line_sep = self.file_manager.getFileAtIndex(index)["line_seperator"]
            self.current_file_index = index
            self.setTitle(os.path.basename(filename))
            try:
                self.mainFrame.txtContent.SetValue(content)
                
            except AttributeError:
                self.mainFrame.txtContent.SetText(content)
                self.mainFrame.txtContent.EmptyUndoBuffer()
                self.mainFrame.txtContent.SetEOLMode(line_sep)
                self.mainFrame.txtContent.ConvertEOLs(line_sep)
                self.mainFrame.txtContent.SetFocusFromKbd()
            
        

     
    def autoindent(self):
        indent=""
        n=0
        l = self.mainFrame.txtContent.GetLine(self.mainFrame.txtContent.GetCurrentLine())

        indent=""
        for char in l:
            
            if char != " " and char != "\t":
                break
            indent += char
    
        self.mainFrame.txtContent.NewLine()
        #self.mainFrame.txtContent.InsertText(self.mainFrame.txtContent.GetCurrentPos(), indent)
        self.mainFrame.txtContent.AddText(indent)
      #self.mainFrame.txtContent.GotoPos(self.mainFrame.txtContent.GetCurrentPos() + n)    

    
    
           


    def continueSearch(self):
        searchValue = self.mainFrame.txtSearch.GetValue()
        print(searchValue)
        case_sensitive = self.mainFrame.chbSearchCaseSensitiv.GetValue()
        as_word = self.mainFrame.chbSearchAsWord.GetValue()
        self.mainFrame.txtContent.SetFocus()
        
        
            

    def onSearch(self, evt):
        self.continueSearch()

      
    def onKeyDown(self, evt):
        if evt.GetKeyCode() == wx.WXK_RETURN:
            self.autoindent()
            
            #self.mainFrame.txtContent.NewLine()
        else:
            evt.Skip()
    

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

        self.mainFrame.cbOpenFiles.Bind(wx.EVT_COMBOBOX, 
        self.onChangecbOpenFiles)

        self.mainFrame.chSyntaxHighlighting.Bind(wx.EVT_CHOICE,
                                                 self.onchSyntaxHighlightingChange)

        self.mainFrame.ribbons.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, 
        self.onRibbonTabChange)

        self.mainFrame.btnOpen.Bind(wx.EVT_BUTTON,
                                             self.onOpenFileDialog)

    
        self.mainFrame.txtContent.Bind(wx.stc.EVT_STC_MODIFIED, self.onChangeText)
        self.mainFrame.txtContent.Bind(wx.EVT_KEY_DOWN, self.onKeyDown)



        self.mainFrame.btnNewFile.Bind(wx.EVT_BUTTON, self.onNewFile)

        self.mainFrame.btnCopy.Bind(wx.EVT_BUTTON, self.onCopy)    
        self.mainFrame.btnPaste.Bind(wx.EVT_BUTTON, self.onPaste)
        
        self.mainFrame.btnUndo.Bind(wx.EVT_BUTTON, self.onUndo)    
        self.mainFrame.btnRedo.Bind(wx.EVT_BUTTON, self.onRedo)
        
        self.mainFrame.chbWrapLines.Bind(wx.EVT_CHECKBOX,
                                         self.onchbWrapLines)
        self.mainFrame.chbDisplayLineEndings.Bind(wx.EVT_CHECKBOX,
                                                  self.onchbDisplayLineEndings)


        self.mainFrame.btnSave.Bind(wx.EVT_BUTTON, self.onBtnSave)
        self.mainFrame.btnSaveAs.Bind(wx.EVT_BUTTON, self.onBtnSaveAs)

        self.mainFrame.btnFindNext.Bind(wx.EVT_BUTTON, self.onSearch)

        


if __name__ == '__main__':
    Main()
