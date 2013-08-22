PrintFile README
----------------

Overview
--------

PrintFile is a freeware utility program that will enable you to print
files fast and easily. The program recognizes plain text, PostScript,
Encapsulated PostScript (EPS) and binary formats. 

Selection of which files to print can be made by the normal Windows file
selection dialog, or by Drag and Drop operations with one or several
files. The latter facilitates batch printing of files. 

PrintFile can also act as a print spooler, watching a specified
directory for files. Whenever a file appears in that directory it will
automatically be printed. 

When printing text files PrintFile makes a configurable page layout of
the text contents. Several logical pages can be placed on one page of
physical paper (referred to as n-up printing). There are also several
other configurable options controlling the layout. Text files can be
printed on any printer that has a Windows printer driver. Text copied
to the clipboard can also be printed in the same manner as text files.
PrintFile can also do user configurable Pretty Printing of text files.
Keywords and comments can be highlighted using different font styles and
colors. This function is primarily intended for source code files. 

Non-text files are sent files directly to a Windows printer. In this
case the program can be seen as a Windows replacement for the DOS
command "copy/b filename LPTx" . As opposed to this DOS command,
PrintFile works well with network printers that have no connection to
any LPTx. This function is mainly intended for printing PostScript files
but may just as well be used for any file created by the "Print to
File" option available for most Windows printer drivers. Such a print
file can for instance be created on a PC without a printer and then be
moved to another PC that has a printer, and here be sent to the printer
using PrintFile.

PostScript files can normally only be printed on PostScript printers. If
a conversion program like Ghostscript is available however, PrintFile
can automatically do a conversion before sending the file to the
printer. The program can also print Encapsulated PostScript Files (EPS).
These files can normally only be inserted into documents and not be
printed directly. It is also possible to control the positioning and
layout of the EPS picture on the printer page. Both EPS files with and
without preview can be handled. Other PostScript features is the
possibility to select an arbitrary range of pages for the printout when
printing multiple page PostScript files and to do n-up printing. 

PrintFile also works well with command line (DOS) programs. It has
several command line options and can read data from command line
standard input, e.g. a command line pipe. A command like "dir | prfile"
can for instance be used to get a n-up printout of a directory listing. 

Both 16-bit (Windows 3.1x) and 32-bit (Windows 95 or later) versions
are available in the distribution.

Documentation is included in a Windows Help file.


Requirements
------------

PrintFile requires a PC running Windows 95 or later

PrintFile is delivered as a zip file archive. Two different archives are
available, one with both a 16 bit and a 32 bit version of PrintFile, and
another that only contains the 32 bit version. 

Installation
------------

In order to install PrintFile you first have to unzip the contents of
the PrintFile zip archive file into a temporary directory. Then run the
setup program. When the installation has finished you can remove the
temporary directory. If you are using WinZip you can do all this just by
pressing the install button in that program. If you are using the
combined 16 and 32 bit archive the installation program will choose the
correct executable for the operating system that you are installing on.
The installation will prompt you for a directory to install PrintFile
into and and if startup menu item should be created.

