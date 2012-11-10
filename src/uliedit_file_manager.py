# -*- coding: utf8 -*-

import os
import wx
import wx.stc
import codecs

class UliEditFileManager:

    def __init__(self):
        self.files = []
        self.empty_file_inc = 0


    def isOpen(self, filename):
        for file in self.files:
            if file["filename"] == filename:
                return True

        return False
    
  
    def saveFile(self, index):
        file = self.getFileAtIndex(index)
        
        # Der Editor arbeitet intern mit UTF8.
        # Encoding des Textes im Editor zum Encoding der Datei konvertieren
        save_file_content = file["content"].encode(file["encoding"])
        
        
        # Wenn die Datei schon einen Dateinamen hat
        if file["filename"] != None and not file["filename"].startswith("untitled"):
            try:
                handle = codecs.open(file["filename"] , "wb", 
                encoding = file["encoding"])
                handle.write(file["content"])
                handle.close()
                self.setModified(index, False)
                return True
            except IOError, e:
                wx.MessageDialog(None,
                        str(e),
                                 os.path.basename(file["filename"]),
                             wx.OK | wx.ICON_ERROR).ShowModal()
                return False
                            
            except OSError, e:
                wx.MessageDialog(None,
                        str(e),
                                 os.path.basename(filename),
                             wx.OK | wx.ICON_ERROR).ShowModal()
                return False
        # Ansonsten Save-As Dialog öffnen
        else:
            pass

  
    
    def setModified(self, index, isModified = True):
        self.files[index]["modified"] = isModified
    
    def newFile(self):
        self.empty_file_inc += 1
        
        
        new_file = {}
        new_file["modified"] = False
        new_file["encoding"] = "utf8"
        new_file["filename"] = "untitled " + str(self.empty_file_inc)
        if os.name == 'posix':
            new_file["line_seperator"] = wx.stc.STC_EOL_LF
        else:
            new_file["line_seperator"] = wx.stc.STC_EOL_CRLF
            
        new_file["content"] = ""
        self.files.append(new_file)
        return len(self.files) - 1

    def getUntitledFilesCount(self):
        count = 0
        for file in self.files:
            if file["filename"].startswith("untitled"):
               count += 1
        return count
        

    def getIndexByFilename(self, filename):
            index = 0
            for file in self.files:
                
                if file["filename"] == filename:
                    return index
                index += 1

            return None

    def getContentByIndex(self, index):
     return self.files[index]["content"]

    def getFileAtIndex(self, index):
        return self.files[index]

    def addFile(self, filename, encoding):
        new_file = {}
        new_file["modified"] = False
        new_file["encoding"] = encoding
        new_file["filename"] = filename
        

        

        try:
            handle = open(filename, 'rb')
            content = handle.read()
            handle.close()
            content = content.decode(encoding)
            new_file["content"] = content
            # Windows:
            if "\r\n" in content:
                new_file["line_seperator"] = wx.stc.STC_EOL_CRLF
            elif "\n" in content:
                new_file["line_seperator"] = wx.stc.STC_EOL_LF
            elif "\r" in content:
                new_file["line_seperator"] = wx.stc.STC_EOL_CR
            else:
                if os.name == 'posix':
                    new_file["line_seperator"] = wx.stc.STC_EOL_LF
                else:
                    new_file["line_seperator"] = wx.stc.STC_EOL_CRLF
           


            self.files.append(new_file)
            
        except IOError, e:
            wx.MessageDialog(None,
                        str(e),
                                 os.path.basename(filename),
                             wx.OK | wx.ICON_ERROR).ShowModal()
            return None

        except OSError:
            wx.MessageDialog(None,
                        u"This file is already opened by another program.",
                                 os.path.basename(filename),
                             wx.OK | wx.ICON_ERROR).ShowModal()
            return None
        
        return len(self.files) - 1


    def closeFileByIndex(self, index):
        self.files.pop(index)
