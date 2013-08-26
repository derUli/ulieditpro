from wxPython.wx import *

from wxPython.html import *

import os,sys



class exHtmlWindow(wxHtmlWindow):

   def __init__(self, parent, id, frame):

      wxHtmlWindow.__init__(self,parent,id)



class exHtmlPanel(wxPanel):

   def __init__(self, parent, id, frame):

      wxPanel.__init__(self,parent,-1)



      self.html = exHtmlWindow(self, -1, frame)



      self.box = wxBoxSizer(wxVERTICAL)

      self.box.Add(self.html, 1, wxGROW)



      self.SetSizer(self.box)
      self.html.LoadPage("http://www.sinus-online.com")
      self.SetAutoLayout(true)



class exFrame (wxFrame):

   def __init__(self, parent, ID, title):

      wxFrame.__init__(self,parent,ID,title,wxDefaultPosition,wxSize(600,750))

      panel = exHtmlPanel(self, -1, self)



class exApp(wxApp):

   def OnInit(self):

      frame = exFrame(NULL, -1, "Example Browser")

      frame.Show(true)

      self.SetTopWindow(frame)

      return true

app = exApp(0)

app.MainLoop()