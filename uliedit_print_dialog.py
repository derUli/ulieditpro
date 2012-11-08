import wx
import uliedit_gui
import os


class PrintDialog:
        def __init__(self, parent, content, title):
                self.parent = parent
                self.content = content
                self.title = os.path.basename(title)
                """ dialog = wx.MessageDialog(parent, "Printing is not implemented",
                                      "Printing",
                                      wx.ICON_WARNING | wx.OK)

                dialog.ShowModal() """
                self.form = uliedit_gui.PrintDialog(parent)
                self.bindEvents()
                self.form.ShowModal()
                


        def onCancel(self, evt):
                self.form.Close()

        def bindEvents(self):
                self.form.btnCancel.Bind(wx.EVT_BUTTON, self.onCancel)
