import wx
import uliedit_gui
import os
import tempfile
import sys
import codecs

class PrintDialog:
        def __init__(self, parent, content, title):
                self.parent = parent
                self.content = content
                self.title = os.path.basename(title)
                self.form = uliedit_gui.PrintDialog(parent)
                self.initFields()
                self.bindEvents()
                self.form.btnPrint.SetFocus()
                self.form.ShowModal()


        def initFields(self):
                enviroment_command = os.environ.get('PRINT_CMD')
                if enviroment_command:
                        self.form.txtCommand.SetValue(enviroment_command)
                elif sys.platform == 'win32':
                    self.form.txtCommand.SetValue("notepad /P %1")
                else:
                    self.form.txtCommand.SetValue("lpr -o portrait -J \"$title\" %1")
                    
                self.form.txtNumberOfCopies.SetValue(1)



        def onCancel(self, evt):
                self.form.Close()
                self.parent.txtContent.SetFocus()

        def onPrint(self, evt):
                count = self.form.txtNumberOfCopies.GetValue()
                command = self.form.txtCommand.GetValue()
                command = command
        
                if command == "":
                        wx.MessageDialog(self.form, "Please Enter a printing command",
                        "Print Error",
                        wx.ICON_ERROR | wx.OK).ShowModal()
                        return

                tmp_file = tempfile.NamedTemporaryFile(delete = False)
                filename = tmp_file.name
                tmp_file.close()
                handle = codecs.open(filename, "wb", encoding = 'utf8')
                handle.write(self.content)
                handle.close()

                # Per lpr-Befehl $count Kopien drucken
                real_command = command.replace("%1", filename)
                real_command = real_command.replace("$title", self.title)
                real_command = real_command.encode("utf8")
                
                for i in range(1, count + 1):
                        os.system(real_command)
                        
                os.unlink(filename)
                self.form.Close()

         
                        
                        
                
        def OnKeyUP(self, event): 
            keyCode = event.GetKeyCode() 
            if keyCode == wx.WXK_ESCAPE:
               self.onCancel(None)
            elif keyCode == wx.WXK_RETURN:
                self.onPrint(None) 
                

        def bindEvents(self):
                self.form.btnCancel.Bind(wx.EVT_BUTTON, self.onCancel)
                self.form.btnPrint.Bind(wx.EVT_BUTTON, self.onPrint)
                self.form.Bind(wx.EVT_CHAR_HOOK, self.OnKeyUP)


