import wx
import uliedit_gui
import os
import tempfile

class PrintDialog:
        def __init__(self, parent, content, title):
                self.parent = parent
                self.content = content.encode("utf8")
                self.title = os.path.basename(title).encode("utf8")
                """ dialog = wx.MessageDialog(parent, "Printing is not implemented",
                                      "Printing",
                                      wx.ICON_WARNING | wx.OK)

                dialog.ShowModal() """
                self.form = uliedit_gui.PrintDialog(parent)
                self.initFields()
                self.bindEvents()
                self.form.ShowModal()


        def initFields(self):
                self.form.txtCommand.SetValue("lpr -J \"" + self.title + "\" %1")
                self.form.txtNumberOfCopies.SetValue(1)



        def onCancel(self, evt):
                self.form.Close()

        def onPrint(self, evt):
                count = self.form.txtNumberOfCopies.GetValue()
                command = self.form.txtCommand.GetValue()
        
                if command == "":
                        wx.MessageDialog(parent, "Please Enter a printing command",
                        "Print Error",
                        wx.ICON_ERROR | wx.OK).ShowModal()
                        return

                tmp_file = tempfile.NamedTemporaryFile(suffix='.txt')
                tmp_file.write(self.content)
                
                # Per lpr-Befehl $count Kopien drucken
                for i in range(1, count + 1):
                        real_command = command.replace("%1", tmp_file.name)
                        os.system(real_command)
                self.form.Close()

                tmp_file.close()
                        
                        
                

                

        def bindEvents(self):
                self.form.btnCancel.Bind(wx.EVT_BUTTON, self.onCancel)
                self.form.btnPrint.Bind(wx.EVT_BUTTON, self.onPrint)
