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
import uliedit_print_dialog
import re
import uliedit_jump_to_dialog

ULIEDIT_FILE_FILTER = "Text Files (*.txt)|*.txt|HTML Documents (*.html)|*.html;*.htm|All Files (*.*)|*"

class Main:

    def __init__(self):
        self.app = wx.App(redirect = False)
        self.fs_enc = sys.getfilesystemencoding()
        self.last_cmd = ""
        self.pwd = os.getcwd()
        try:
            os.chdir(os.path.dirname(sys.argv[0]))
        except OSError:
            pass
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
        
        self.mainFrame.txtContent.ClearAll()
        self.file_manager.getFileAtIndex(self.current_file_index)["modified"] = False

    def parseCommandLineArgs(self, args):
        if len(args) > 1:
            filename = args[1].decode(self.fs_enc)
            filename = os.path.abspath(filename)
            if not os.path.exists(filename):
                try:
                    open(filename, "w").close()
                except OSError:
                    pass
                except IOError:
                    pass
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
                               style = wx.OPEN | wx.FD_FILE_MUST_EXIST, wildcard = ULIEDIT_FILE_FILTER)

        if dialog.ShowModal() == wx.ID_OK:
            self.last_path = dialog.GetPath()
            self.last_path = os.path.dirname(self.last_path)
            self.saveLastPath(self.last_path)
            self.openFile(dialog.GetPath())
            


    def onBtnIncludeFile(self, evt):
        self.includeFile()


    def onBtnInsertImage(self, evt):
        dialog = wx.TextEntryDialog(None, "Insert Image:", "Insert Image", "", style=wx.OK|wx.CANCEL)
        if dialog.ShowModal() == wx.ID_OK:
           htmlCode = '<img src="' + dialog.GetValue() + '" border=0>'
           self.mainFrame.txtContent.AddText(htmlCode)
           self.mainFrame.txtContent.SetFocus()


    def includeFile(self):
        self.mainFrame.txtContent.SetFocus()
        dialog = wx.FileDialog(parent = self.mainFrame,
        message = "Include File",
        defaultDir = self.last_path,
        style = wx.OPEN | wx.FD_FILE_MUST_EXIST, wildcard = ULIEDIT_FILE_FILTER)

        if dialog.ShowModal() == wx.ID_OK:
            self.last_path = dialog.GetPath()
            filename = dialog.GetPath()
            self.last_path = os.path.dirname(self.last_path)
            content = self.file_manager.getContentFromFile(filename)
            encoding = uliedit_charset_helper.detect_encoding(filename)
            if encoding:

                content = content.decode(encoding)
                tmp = self.file_manager.getFileAtIndex(self.current_file_index)
                line_seperator = tmp["line_seperator"]
                
                self.mainFrame.txtContent.AddText(content)
                self.mainFrame.txtContent.ConvertEOLs(line_seperator)
                self.mainFrame.txtContent.SetFocus()
                return True
                
            else:
                wx.MessageDialog(None,
                        u"Kann das Encoding nicht erkennen!",
                                 os.path.basename(filename),
                        wx.OK | wx.ICON_WARNING).ShowModal()
                return False




    def openFile(self, filename):
        filename = os.path.abspath(filename)
        encoding = uliedit_charset_helper.detect_encoding(filename)
        if encoding:
            """ wx.MessageDialog(None,
                        encoding, "Encoding of " + os.path.basename(filename),
                        wx.OK | wx.ICON_INFORMATION).ShowModal() """
                        

            if self.file_manager.isOpen(filename):
                wx.MessageDialog(None,
                        u"This file is already open.",
                                 os.path.basename(filename),
                        wx.OK | wx.ICON_WARNING, wildcard = ULIEDIT_FILE_FILTER).ShowModal()
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
                        self.mainFrame.txtContent.SetFocus()
                        self.file_manager.getFileAtIndex(tmp)["modified"] = False
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
                               style = wx.SAVE | wx.FD_OVERWRITE_PROMPT, wildcard = ULIEDIT_FILE_FILTER)

        if dialog.ShowModal() == wx.ID_OK:
            self.last_path = dialog.GetPath()
            self.file_manager.getFileAtIndex(self.current_file_index)["filename"] = self.last_path
            self.setTitle(dialog.GetPath())
            self.mainFrame.cbOpenFiles.Clear()
            for file in self.file_manager.files:
                self.mainFrame.cbOpenFiles.Append(file["filename"])
            self.mainFrame.cbOpenFiles.SetStringSelection(self.last_path)
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


    def onBtnInfo(self, evt):
        info_string = u"UliEdit Pro 1.4\n\n"
        info_string += u"A programmers text editor\n\n"
        info_string += u"© 2012 by Ulrich Schmidt (admin@deruli.de)\n\n"
        info_string += u"For more software take a look at:\n"
        info_string += u"www.deruli.de\nwww.uligames.de"
        
        wx.MessageDialog(self.mainFrame,
                         info_string, "Info",
                         wx.ICON_INFORMATION | wx.OK).ShowModal()

        self.mainFrame.txtContent.SetFocus()

        
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
        
              
               


    def shortcutHandler(self, evt):
        if evt.GetKeyCode() == wx.WXK_F3:
            self.continueSearch()
            return
        elif evt.ControlDown() and evt.AltDown():
            evt.Skip()
            return

            
        elif evt.ControlDown():
            # print(evt.GetKeyCode())
            # ctrl + O
            if evt.GetKeyCode() == 79:
                self.openFileDialog()
            # ctrol + s
            elif evt.GetKeyCode() == 83:
                self.save_current_file()
                return
            # ctrl + Q
            elif evt.GetKeyCode() == 81:
                self.askForSaveOnQuit()
                return
            # ctrl + n
            elif evt.GetKeyCode() == 78:
                self.openEmptyFile()
                return
            # ctrl + f
            elif evt.GetKeyCode() == 70:
                self.mainFrame.ribbons.SetSelection(1)
                self.mainFrame.txtSearch.SetFocus()
                self.mainFrame.txtSearch.SelectAll()
                return
            # ctrl + p
            elif evt.GetKeyCode() == 80:
                self.openPrintDialog()
                return
            #ctrl + a
            elif evt.GetKeyCode() == 65:
                self.mainFrame.txtContent.SelectAll()
                return
            else:
                evt.Skip()

        else:
            evt.Skip()



            


        
                   


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
            self.mainFrame.txtContent.SetMarginWidth(1, 70)
            
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
        index = self.current_file_index
        file = self.file_manager.getFileAtIndex(index)
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
                    self.file_manager.closeFileByIndex(index)
                    self.mainFrame.cbOpenFiles.Clear()
            
                    for file in self.file_manager.files:
                        self.mainFrame.cbOpenFiles.Append(file["filename"])

                    if self.current_file_index > 0:
                        self.current_file_index -= 1


                    if len(self.file_manager.files) > 0:
                        self.mainFrame.cbOpenFiles.SetStringSelection(self.file_manager.getFileAtIndex(self.current_file_index)["filename"])
                        self.changeCurrentFile(self.mainFrame.cbOpenFiles.GetValue())
                        return
                    else:
                        os.chdir(self.pwd)
                        wx.TheClipboard.Flush()
                        sys.exit(0)
                 else:
                     return



            elif result == wx.ID_NO:
                self.file_manager.closeFileByIndex(index)
                self.mainFrame.cbOpenFiles.Clear()
            
                for file in self.file_manager.files:
                    self.mainFrame.cbOpenFiles.Append(file["filename"])


                if self.current_file_index > 0:
                    self.current_file_index -= 1

                if len(self.file_manager.files) > 0:
                    self.mainFrame.cbOpenFiles.SetStringSelection(self.file_manager.getFileAtIndex(self.current_file_index)["filename"])
                    self.changeCurrentFile(self.mainFrame.cbOpenFiles.GetValue())
                    return
                else:
                    os.chdir(self.pwd)
                    wx.TheClipboard.Flush()
                    sys.exit(0)
                

        else:
            self.file_manager.closeFileByIndex(index)
            self.mainFrame.cbOpenFiles.Clear()
            
            for file in self.file_manager.files:
                self.mainFrame.cbOpenFiles.Append(file["filename"])


            if len(files) > 0:
                self.current_file_index -= 1
                self.mainFrame.cbOpenFiles.SetStringSelection(self.file_manager.getFileAtIndex(self.current_file_index)["filename"])
                self.changeCurrentFile(self.mainFrame.cbOpenFiles.GetValue())
            else:
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
            old_index = self.current_file_index

            index = self.file_manager.getIndexByFilename(filename)
            modified_before = self.file_manager.files[old_index]["modified"]
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
                self.mainFrame.txtContent.SetFocus()

                if not modified_before:
                    self.file_manager.files[old_index]["modified"] = False
                    
            
        
    def openPrintDialog(self):
        uliedit_print_dialog.PrintDialog(self.mainFrame,
        self.file_manager.getContentByIndex(self.current_file_index),
        self.file_manager.getFileAtIndex(self.current_file_index)["filename"])

    def onBtnPrint(self, evt):
        self.openPrintDialog()

    def onBtnJumpToPosition(self, evt):
        self.mainFrame.txtContent.SetFocus()
        self.openJumpToDialog()


    def openJumpToDialog(self):
        uliedit_jump_to_dialog.JumpToDialog(self.mainFrame, self.mainFrame.txtContent)

     
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

    









    def SearchAndReplace(self, count):
        self.mainFrame.txtContent.SetFocus()
        ctrl = self.mainFrame.txtContent
        if count == 1:
            ctrl.GotoPos(0)
            ctrl.SearchAnchor()
            
        searchValue = self.mainFrame.txtSearch.GetValue()
        if searchValue == "":
            return


        replaceValue = self.mainFrame.txtReplace.GetValue()

        if searchValue == replaceValue:
            return



        
        flags = wx.stc.STC_FIND_WORDSTART
        case_sensitive = self.mainFrame.chbSearchCaseSensitiv.GetValue()
        as_word = self.mainFrame.chbSearchAsWord.GetValue()
        self.mainFrame.txtContent.SetFocus()

        new_text = ctrl.GetText()

        if case_sensitive:
            new_text = new_text.replace(searchValue, replaceValue)
        else:
            pattern = re.compile(re.escape(searchValue), re.IGNORECASE)
            new_text = pattern.sub(replaceValue, new_text)
        ctrl.SetText(new_text)


               
         


    def FindNext(self, text, flags, ctrl):
        """Find the next occurance of the text"""
        #set the search anchor
        pos = ctrl.GetCurrentPos()
        if pos==ctrl.GetLength():
            ctrl.SetCurrentPos(0)
        else:
            ctrl.SetCurrentPos(pos+1)
  
        ctrl.SearchAnchor()
        spos = ctrl.SearchNext(flags,text)
        ctrl.EnsureCaretVisible()
        if spos==-1:
            ctrl.SetCurrentPos(pos)
            return False
        else:
            return True 
           


    def continueSearch(self):
        self.mainFrame.txtContent.SetFocus()
        ctrl = self.mainFrame.txtContent
        ctrl.SetVisiblePolicy(wx.stc.STC_VISIBLE_SLOP, 7)
        ctrl.SetCaretLineVisible(False)
        searchValue = self.mainFrame.txtSearch.GetValue()
        flags = 0
        case_sensitive = self.mainFrame.chbSearchCaseSensitiv.GetValue()
        as_word = self.mainFrame.chbSearchAsWord.GetValue()
        self.mainFrame.txtContent.SetFocus()

        if as_word:
            flags = flags | wx.stc.STC_FIND_WHOLEWORD

        if case_sensitive:
            flags = flags | wx.stc.STC_FIND_MATCHCASE


        """ oldpos = ctrl.GetCurrentPos()
        b,e = ctrl.GetSelectionStart(),ctrl.GetSelectionEnd()
        ctrl.SearchAnchor()
        self.mainFrame.txtContent.SearchNext(flags, searchValue)
        """
        #ctrl.SearchAnchor()
        #ipos = ctrl.SearchNext(flags, searchValue)
        #ctrl.EnsureCaretVisible()
        if self.FindNext(searchValue, flags, ctrl):
            pass
        else:
            
            wx.MessageDialog(self.mainFrame,
            "You've reached the end of the document",
            "Search",
            wx.ICON_WARNING | wx.OK).ShowModal()
            ctrl.GotoPos(0)
        
        """
        if ipos == -1:
            ctrl.GotoPos(0)
            ctrl.SearchAnchor()
        else:
            ctrl.GotoPos(ipos)
        
        if ipos == oldpos:
            i = ctrl.GetCurrentPos() + len(searchValue)
            ctrl.SetSelection(i,i)
            ctrl.SearchAnchor()
            ipos = ctrl.SearchNext(flags, searchValue)
            if ipos == -1:
                 wx.MessageDialog(self.mainFrame,
                "You've reached the end of the document",
                             "Search",
                             wx.ICON_WARNING | wx.OK).ShowModal()


            
        else:
            ipos = ctrl.SearchPrev(flags, searchValue)
            if ipos == oldpos:
                i = ctrl.GetCurrentPos() - len(searchValue)
                ctrl.SetSelection(i,i)
                ctrl.SearchAnchor()
                ipos = ctrl.SearchPrev(flags, searchValue)"""
                

    

                



 


    def onbtnRunShellCommand(self, evt):
        
        result = wx.TextEntryDialog(self.mainFrame, 
                                    'Command:',
                                    'Run shell command', 
                                    self.last_cmd, style=wx.OK|wx.CANCEL)
        if result.ShowModal() == wx.ID_OK:
            self.last_cmd = result.GetValue()
            os.system(self.last_cmd)
        self.mainFrame.txtContent.SetFocus()
            

    def onSearch(self, evt):
        self.continueSearch()


    def onReplace(self, evt):
        self.SearchAndReplace(1)

    def onTxtSearchKeyDown(self, evt):
        if evt.GetKeyCode() == wx.WXK_RETURN:
            self.continueSearch()
        else:
            evt.Skip()


    def onBtnStatistic(self, evt):
        file_length = self.mainFrame.txtContent.GetTextLength()
        line_count = self.mainFrame.txtContent.GetLineCount()
        statistic_string = "Length: " + str(file_length)
        statistic_string += "\n"
        statistic_string += "Lines: " + str(line_count)

        filename = self.file_manager.getFileAtIndex(self.current_file_index)
        filename = filename["filename"]
        filename = os.path.basename(filename)

        wx.MessageDialog(self.mainFrame, statistic_string, filename,
                         wx.ICON_INFORMATION | wx.OK).ShowModal()

        self.mainFrame.txtContent.SetFocus()


        
      
    def onKeyDown(self, evt):
        if evt.GetKeyCode() == wx.WXK_RETURN:
            self.autoindent()
            #self.mainFrame.txtContent.NewLine()
        else:
            self.shortcutHandler(evt)
            #evt.Skip()
    

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
        self.mainFrame.txtSearch.Bind(wx.EVT_KEY_DOWN, self.onTxtSearchKeyDown)



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
        self.mainFrame.btnPrint.Bind(wx.EVT_BUTTON, self.onBtnPrint)

        self.mainFrame.btnFindNext.Bind(wx.EVT_BUTTON, self.onSearch)
        self.mainFrame.btnReplace.Bind(wx.EVT_BUTTON, self.onReplace)

        self.mainFrame.btnJumpToPosition.Bind(wx.EVT_BUTTON, self.onBtnJumpToPosition)

        self.mainFrame.btnIncludeFile.Bind(wx.EVT_BUTTON, self.onBtnIncludeFile)
        self.mainFrame.btnStatistic.Bind(wx.EVT_BUTTON, self.onBtnStatistic)
        self.mainFrame.btnRunShellCommand.Bind(wx.EVT_BUTTON, self.onbtnRunShellCommand)
        
        self.mainFrame.btnInfo.Bind(wx.EVT_BUTTON, self.onBtnInfo)

        self.mainFrame.btnInsertImage.Bind(wx.EVT_BUTTON, self.onBtnInsertImage)

        


if __name__ == '__main__':
    Main()
