import wx
import uliedit_gui
import os
import tempfile
import sys
import codecs

class JumpToDialog:
        def __init__(self, parent, ctrl):
                self.ctrl = ctrl
                self.form = uliedit_gui.JumpToDialog(parent)
                self.bindEvents()
                self.form.ShowModal()



        def onOK(self, evt):
                pos = self.form.spnPosition.GetValue()
                self.form.Close()
                self.ctrl.SetFocus()
                self.ctrl.GotoPos(pos)


        def bindEvents(self):
                self.form.btnJumpTo.Bind(wx.EVT_BUTTON,
                                         self.onOK)
