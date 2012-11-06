# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.richtext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"No Title", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.FULL_REPAINT_ON_RESIZE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.ribbons = wx.Notebook( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0|wx.FULL_REPAINT_ON_RESIZE )
		self.m_panel1 = wx.Panel( self.ribbons, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnOpen = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"images/open.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer2.Add( self.btnOpen, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.btnSave = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"images/save.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer2.Add( self.btnSave, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.btnSaveAs = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"images/bigfolder.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer2.Add( self.btnSaveAs, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.btnCopy = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"images/Copy-icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer2.Add( self.btnCopy, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.btnPaste = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"images/paste.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer2.Add( self.btnPaste, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer2.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.btnPrint = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"images/print.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer2.Add( self.btnPrint, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		self.ribbons.AddPage( self.m_panel1, u"START", True )
		self.m_panel2 = wx.Panel( self.ribbons, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel2.SetSizer( bSizer3 )
		self.m_panel2.Layout()
		bSizer3.Fit( self.m_panel2 )
		self.ribbons.AddPage( self.m_panel2, u"SEARCH && REPLACE", False )
		self.m_panel3 = wx.Panel( self.ribbons, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		cbOpenFilesChoices = [ u"test", u"test 2" ]
		self.cbOpenFiles = wx.ComboBox( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cbOpenFilesChoices, wx.CB_SIMPLE|wx.CB_SORT|wx.TE_PROCESS_ENTER )
		bSizer4.Add( self.cbOpenFiles, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel3.SetSizer( bSizer4 )
		self.m_panel3.Layout()
		bSizer4.Fit( self.m_panel3 )
		self.ribbons.AddPage( self.m_panel3, u"FILES", False )
		
		bSizer1.Add( self.ribbons, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_richText1 = wx.richtext.RichTextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer1.Add( self.m_richText1, 3, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel5.SetSizer( bSizer1 )
		self.m_panel5.Layout()
		bSizer1.Fit( self.m_panel5 )
		bSizer5.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

