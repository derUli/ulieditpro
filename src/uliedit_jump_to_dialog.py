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
            self.form.spnPosition.SetValue(self.ctrl.GetCurrentLine() + 1)
            self.bindEvents()
            self.form.spnPosition.SetFocus();
            self.form.ShowModal()
        
        def onCancel(self, evt):
            self.form.Close()
            self.ctrl.SetFocus()
        
        def OnKeyUP(self, event): 
            keyCode = event.GetKeyCode() 
            if keyCode == wx.WXK_ESCAPE: 
               self.onCancel(None)
            elif keyCode == wx.WXK_RETURN:
                self.onOK(None) 


        def onOK(self, evt):
            pos = self.form.spnPosition.GetValue() - 1
            self.form.Close()
            self.ctrl.SetFocus()
            self.ctrl.GotoLine(pos)


        def bindEvents(self):
            self.form.btnJumpTo.Bind(wx.EVT_BUTTON,
                                         self.onOK)
                                        
            self.form.Bind(wx.EVT_CHAR_HOOK, self.OnKeyUP)

