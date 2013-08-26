# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.html

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"No Title", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.FULL_REPAINT_ON_RESIZE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.pn_main = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.ribbons = wx.Notebook( self.pn_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0|wx.FULL_REPAINT_ON_RESIZE )
		self.m_panel1 = wx.Panel( self.ribbons, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnNewFile = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"images/newFile.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer2.Add( self.btnNewFile, 0, wx.ALL, 1 )
		
		self.btnOpen = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"images/open.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer2.Add( self.btnOpen, 0, wx.ALL, 1 )
		
		self.btnSave = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"images/save.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer2.Add( self.btnSave, 0, wx.ALL, 1 )
		
		self.btnSaveAs = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"images/bigfolder.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer2.Add( self.btnSaveAs, 0, wx.ALL, 1 )
		
		self.m_staticline1 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.btnCopy = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"images/Copy-icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer2.Add( self.btnCopy, 0, wx.ALL, 1 )
		
		self.btnPaste = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"images/paste.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer2.Add( self.btnPaste, 0, wx.ALL, 1 )
		
		self.m_staticline2 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer2.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.btnUndo = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"images/undo.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer2.Add( self.btnUndo, 0, wx.ALL, 1 )
		
		self.btnRedo = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"images/redo.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer2.Add( self.btnRedo, 0, wx.ALL, 1 )
		
		self.m_staticline3 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer2.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.btnPrint = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"images/print.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer2.Add( self.btnPrint, 0, wx.ALL, 1 )
		
		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		self.ribbons.AddPage( self.m_panel1, u"START", True )
		self.m_panel2 = wx.Panel( self.ribbons, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Search For:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer12.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.txtSearch = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer12.Add( self.txtSearch, 10, wx.ALL, 5 )
		
		
		bSizer12.AddSpacer( ( 0, 0), 1, 0, 5 )
		
		bSizer11.Add( bSizer12, 1, wx.EXPAND, 0 )
		
		bSizer121 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText21 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Replace:    ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		bSizer121.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.txtReplace = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer121.Add( self.txtReplace, 10, wx.ALL, 5 )
		
		
		bSizer121.AddSpacer( ( 0, 0), 1, 0, 5 )
		
		bSizer11.Add( bSizer121, 1, wx.EXPAND, 5 )
		
		bSizer3.Add( bSizer11, 3, wx.EXPAND, 5 )
		
		bSizer91 = wx.BoxSizer( wx.VERTICAL )
		
		self.chbSearchAsWord = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"As whole Word", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer91.Add( self.chbSearchAsWord, 0, wx.ALL, 5 )
		
		self.chbSearchCaseSensitiv = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"Case Sensitive", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer91.Add( self.chbSearchCaseSensitiv, 0, wx.ALL, 5 )
		
		bSizer3.Add( bSizer91, 1, wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnFindNext = wx.Button( self.m_panel2, wx.ID_ANY, u"Find Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnFindNext.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer10.Add( self.btnFindNext, 0, wx.ALL, 5 )
		
		self.btnReplace = wx.Button( self.m_panel2, wx.ID_ANY, u"Replace", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnReplace.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer10.Add( self.btnReplace, 0, wx.ALL, 5 )
		
		bSizer3.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		self.m_panel2.SetSizer( bSizer3 )
		self.m_panel2.Layout()
		bSizer3.Fit( self.m_panel2 )
		self.ribbons.AddPage( self.m_panel2, u"SEARCH && REPLACE", False )
		self.m_panel3 = wx.Panel( self.ribbons, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		cbOpenFilesChoices = [ u"test", u"test 2" ]
		self.cbOpenFiles = wx.ComboBox( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cbOpenFilesChoices, wx.CB_READONLY|wx.CB_SIMPLE|wx.TE_PROCESS_ENTER )
		bSizer4.Add( self.cbOpenFiles, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel3.SetSizer( bSizer4 )
		self.m_panel3.Layout()
		bSizer4.Fit( self.m_panel3 )
		self.ribbons.AddPage( self.m_panel3, u"FILES", False )
		self.m_panel5 = wx.Panel( self.ribbons, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Syntax Highlighting:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer8.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		chSyntaxHighlightingChoices = []
		self.chSyntaxHighlighting = wx.Choice( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chSyntaxHighlightingChoices, 0 )
		self.chSyntaxHighlighting.SetSelection( 0 )
		bSizer8.Add( self.chSyntaxHighlighting, 0, wx.ALL, 5 )
		
		bSizer7.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.chbWrapLines = wx.CheckBox( self.m_panel5, wx.ID_ANY, u"Wrap Lines", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.chbWrapLines, 0, wx.ALL, 5 )
		
		self.chbDisplayLineEndings = wx.CheckBox( self.m_panel5, wx.ID_ANY, u"Display Line Endings", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.chbDisplayLineEndings, 0, wx.ALL, 5 )
		
		bSizer7.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		self.m_panel5.SetSizer( bSizer7 )
		self.m_panel5.Layout()
		bSizer7.Fit( self.m_panel5 )
		self.ribbons.AddPage( self.m_panel5, u"VIEW", False )
		self.m_panel7 = wx.Panel( self.ribbons, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnStatistic = wx.Button( self.m_panel7, wx.ID_ANY, u"Statistics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnStatistic.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer21.Add( self.btnStatistic, 2, wx.ALL|wx.EXPAND, 5 )
		
		self.btnIncludeFile = wx.Button( self.m_panel7, wx.ID_ANY, u"Include File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnIncludeFile.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer21.Add( self.btnIncludeFile, 2, wx.ALL|wx.EXPAND, 5 )
		
		self.btnJumpToPosition = wx.Button( self.m_panel7, wx.ID_ANY, u"Goto Line", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnJumpToPosition.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer21.Add( self.btnJumpToPosition, 2, wx.ALL|wx.EXPAND, 5 )
		
		self.btnRunShellCommand = wx.Button( self.m_panel7, wx.ID_ANY, u"Run Shell Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnRunShellCommand.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer21.Add( self.btnRunShellCommand, 2, wx.ALL|wx.EXPAND, 5 )
		
		bSizer20.Add( bSizer21, 4, wx.EXPAND, 5 )
		
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer20.Add( bSizer22, 1, wx.EXPAND, 5 )
		
		self.m_panel7.SetSizer( bSizer20 )
		self.m_panel7.Layout()
		bSizer20.Fit( self.m_panel7 )
		self.ribbons.AddPage( self.m_panel7, u"TOOLS", False )
		self.m_panel10 = wx.Panel( self.ribbons, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnInsertImage = wx.BitmapButton( self.m_panel10, wx.ID_ANY, wx.Bitmap( u"images/image.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer26.Add( self.btnInsertImage, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel10.SetSizer( bSizer26 )
		self.m_panel10.Layout()
		bSizer26.Fit( self.m_panel10 )
		self.ribbons.AddPage( self.m_panel10, u"HTML", False )
		self.m_panel8 = wx.Panel( self.ribbons, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnHelp = wx.BitmapButton( self.m_panel8, wx.ID_ANY, wx.Bitmap( u"images/help.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer19.Add( self.btnHelp, 0, wx.ALL, 5 )
		
		self.btnInfo = wx.BitmapButton( self.m_panel8, wx.ID_ANY, wx.Bitmap( u"images/info.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer19.Add( self.btnInfo, 0, wx.ALL, 5 )
		
		self.m_panel8.SetSizer( bSizer19 )
		self.m_panel8.Layout()
		bSizer19.Fit( self.m_panel8 )
		self.ribbons.AddPage( self.m_panel8, u"HELP", False )
		
		bSizer1.Add( self.ribbons, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.txtContent = wx.stc.StyledTextCtrl( self.pn_main, wx.ID_ANY)
		bSizer1.Add( self.txtContent, 3, wx.ALL|wx.EXPAND, 5 )
		
		self.pn_main.SetSizer( bSizer1 )
		self.pn_main.Layout()
		bSizer1.Fit( self.pn_main )
		bSizer5.Add( self.pn_main, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer5 )
		self.Layout()
		self.statusbar = self.CreateStatusBar( 2, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class PrintDialog
###########################################################################

class PrintDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Print", pos = wx.DefaultPosition, size = wx.Size( 556,208 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText4 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Number of copies:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer16.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.txtNumberOfCopies = wx.SpinCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 200, 1 )
		bSizer16.Add( self.txtNumberOfCopies, 0, wx.ALL, 5 )
		
		bSizer15.Add( bSizer16, 0, wx.EXPAND, 5 )
		
		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Command:            ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer17.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.txtCommand = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.txtCommand, 5, wx.ALL, 5 )
		
		
		bSizer17.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btnAvailPrinters = wx.Button( self.m_panel6, wx.ID_ANY, u"Available Printers", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnAvailPrinters.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer17.Add( self.btnAvailPrinters, 0, wx.ALL, 5 )
		
		
		bSizer17.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer15.Add( bSizer17, 1, wx.EXPAND, 5 )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer18.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btnCancel = wx.Button( self.m_panel6, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnCancel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer18.Add( self.btnCancel, 0, wx.ALL, 5 )
		
		
		bSizer18.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btnPrint = wx.Button( self.m_panel6, wx.ID_ANY, u"Print", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnPrint.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer18.Add( self.btnPrint, 0, wx.ALL, 5 )
		
		
		bSizer18.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer15.Add( bSizer18, 1, wx.EXPAND, 5 )
		
		self.m_panel6.SetSizer( bSizer15 )
		self.m_panel6.Layout()
		bSizer15.Fit( self.m_panel6 )
		bSizer14.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer14 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class JumpToDialog
###########################################################################

class JumpToDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Goto Line", pos = wx.DefaultPosition, size = wx.Size( 278,194 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer26.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Goto Line:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer24.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.spnPosition = wx.SpinCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.SP_WRAP, 0, 2147483647, 0 )
		bSizer24.Add( self.spnPosition, 0, wx.ALL, 5 )
		
		
		bSizer24.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btnJumpTo = wx.Button( self.m_panel10, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.btnJumpTo, 0, wx.ALL, 5 )
		
		bSizer26.Add( bSizer24, 1, wx.EXPAND, 5 )
		
		
		bSizer26.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_panel10.SetSizer( bSizer26 )
		self.m_panel10.Layout()
		bSizer26.Fit( self.m_panel10 )
		bSizer25.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer25 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class HelpDialog
###########################################################################

class HelpDialog ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"man", pos = wx.DefaultPosition, size = wx.Size( 634,418 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		self.htmlPane = wx.html.HtmlWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.html.HW_SCROLLBAR_AUTO )
		bSizer27.Add( self.htmlPane, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.SetSizer( bSizer27 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class availablePrinterDialog
###########################################################################

class availablePrinterDialog ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Available Printers", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer28 = wx.BoxSizer( wx.VERTICAL )
		
		self.txtPrinters = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer28.Add( self.txtPrinters, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.SetSizer( bSizer28 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

