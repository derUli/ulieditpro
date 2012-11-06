import uliedit_gui
import wx

class Main:

    def __init__(self):
        self.app = wx.App()
        self.mainFrame = uliedit_gui.MainFrame(None)
        self.mainFrame.Show(True)
        self.app.MainLoop()
        


if __name__ == '__main__':
    Main()
