import wx



class PrintDialog:
        def __init__(self, parent, content):
                self.parent = parent
                self.content = content
                dialog = wx.MessageDialog(parent, "Printing is not implemented",
                                      "Printing",
                                      wx.ICON_WARNING | wx.OK)

                dialog.ShowModal()
