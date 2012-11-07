import wx
import wx.stc


def getLexer(name):
    lexer_list = {"ADA" : wx.stc.STC_LEX_ADA,
              "ASP" : wx.stc.STC_LEX_HTML,
              "AVE" : wx.stc.STC_LEX_AVE,
              "BAAN" : wx.stc.STC_LEX_BAAN,
              "BATCH" : wx.stc.STC_LEX_BATCH,
              "BULLANT" : wx.stc.STC_LEX_BULLANT,
              "CONF" : wx.stc.STC_LEX_CONF,
              "C++"  : wx.stc.STC_LEX_CPP,
              "DIFF" : wx.stc.STC_LEX_DIFF,
              "EIFFEL" : wx.stc.STC_LEX_EIFFEL,
              "EIFFELKW" : wx.stc.STC_LEX_EIFFELKW,
              "ERRORLIST" : wx.stc.STC_LEX_ERRORLIST,
              "HTML" : wx.stc.STC_LEX_HTML,
              "LATEX" : wx.stc.STC_LEX_LATEX,
              "LISP" : wx.stc.STC_LEX_LISP,
              "LUA" : wx.stc.STC_LEX_LISP,
              "MAKEFILE" : wx.stc.STC_LEX_MAKEFILE,
              "MATLABE" : wx.stc.STC_LEX_MATLAB,
              "NNCRONTAB" : wx.stc.STC_LEX_NNCRONTAB,
              "PLAIN" : wx.stc.STC_LEX_NULL,
              "PASCAL" : wx.stc.STC_LEX_PASCAL,
              "PERL" : wx.stc.STC_LEX_PERL,
              "PHP" : wx.stc.STC_LEX_HTML,
              "PROPERTIES" : wx.stc.STC_LEX_PROPERTIES,
              "PYTHON" : wx.stc.STC_LEX_PYTHON,
              "RUBY" : wx.stc.STC_LEX_RUBY,
              "TCL" : wx.stc.STC_LEX_TCL,
              "VB" : wx.stc.STC_LEX_VB,
              "VBSCRIPT" : wx.stc.STC_LEX_VBSCRIPT,
              "XML" : wx.stc.STC_LEX_XML,
              

              }

    return lexer_list[name]
