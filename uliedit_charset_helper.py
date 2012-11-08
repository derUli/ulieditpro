import wx

def detect_encoding(filename):
    # gather the encodings you think that the file may be
    # encoded inside a tuple
    encodings = ('utf-8', 'windows-1252', 'iso-8859-1', 'iso-8859-15')

    # try to open the file and exit if some IOError occurs
    try:
        f = open(filename, 'r').read()
    except Exception:
       wx.MessageDialog(None,
                        u"Can't read " + filename,
                        "Input/Output Error",
                        wx.OK | wx.ICON_ERROR).ShowModal()
       return None
        

    # now start iterating in our encodings tuple and try to
    # decode the file
    for enc in encodings:
        try:
            # try to decode the file with the first encoding
            # from the tuple.
            # if it succeeds then it will reach break, so we
            # will be out of the loop (something we want on
            # success).
            # the data variable will hold our decoded text
            data = f.decode(enc)
            return enc
        except Exception:
            pass

    return None
