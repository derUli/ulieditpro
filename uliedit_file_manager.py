class UliEditFileManager:

    def __init__(self):
        self.files = []


    def isOpen(self, filename):
        for file in self.files:
            if file["filename"] == filename:
                return True

        return False
    
    
    def newFile(self):
        number = self.getUntitledFilesCount() + 1
        
        new_file = {}
        new_file["modified"] = False
        new_file["encoding"] = "utf8"
        new_file["filename"] = "untitled " + str(number)
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
            handle = open(filename, 'r')
            content = handle.read()
            handle.close()
            content = content.decode(encoding)
            new_file["content"] = content

            self.files.append(new_file)
            
        except IOError:
            wx.MessageDialog(None,
                        u"Input/Output Error",
                                 os.path.basename(filename),
                             wx.OK | wx.ERROR).ShowModal()
            return None

        except OSError:
            wx.MessageDialog(None,
                        u"This file is already opened by another program.",
                                 os.path.basename(filename),
                             wx.OK | wx.ERROR).ShowModal()
            return None
        
        return len(self.files) - 1


    def closeFileByIndex(self, index):
        self.files.pop(index)
