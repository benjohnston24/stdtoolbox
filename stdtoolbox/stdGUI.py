#! /usr/bin/env python
"""
"""
__author__ = "Ben Johnston"
__revision__ = "0.1"
__date__ = "Mon Apr 14 22:19:34 EST 2014"
__license__ = "GPL"


##IMPORTS####################################################################
from Tkinter import Frame, Menu, Label, LabelFrame, StringVar
from Tkinter import Entry as tkEntry, Checkbutton
from ttk import Button, Entry, Scrollbar, Progressbar, Combobox
#############################################################################

##CONSTANTS##################################################################
DEFAULT_BACKGROUND = 'white'
DEFAULT_FOREGROUND = 'black'
TABLE_HEADER_BACKGROUND = "#B6B6B6"
TABLE_HEADER_TEXT_COLOUR = 'black'
#############################################################################


class stdGUI(Frame):
    """!
    A class to define a standard user interface.  This class will allow
    GUI's to be quickly built and configured.
    """
    def __init__(self, parent):
        """!
        A constructor for the class
        @param self The pointer for the object
        @param parent The parent Tkinter.Tk object
        Edit etc menu to the root window.
        """
        #Initialise the inherited class
        Frame.__init__(self, parent)
        ##@var parent
        #The parent window for the GUI
        self.parent = parent
        #Configure the root background
        self.parent.configure(background=DEFAULT_BACKGROUND)

    def add_menu(self, parent):
        """!
        This method is used to add the File, Edit, View, Tools and Help
        menu to the parent.
        @param self The pointer for the object
        @param parent The parent window destination for the toolbar
        """
        ##@var menu_bar
        #The menu bar object for the class
        self.menu_bar = Menu(parent)
        ##@var file_menu
        #The file menu for the object
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        ##@var edit_menu
        #The edit menu for the object
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        ##@var view_menu
        #The view menu for the object
        self.view_menu = Menu(self.menu_bar, tearoff=0)
        ##@var tools_menu
        #The tool menu for the object
        self.tools_menu = Menu(self.menu_bar, tearoff=0)
        ##@var help_menu
        #The help menu for the object
        self.help_menu = Menu(self.menu_bar, tearoff=0)
        #Add cascade
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.menu_bar.add_cascade(label="View", menu=self.view_menu)
        self.menu_bar.add_cascade(label="Tools", menu=self.tools_menu)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        #Add file menu commands
        self.file_menu.add_command(label="New",
                                   command=self.new_cmd,
                                   accelerator="F1")
        self.file_menu.add_command(label="Open", command=self.open_cmd)
        self.file_menu.add_command(label="Save", command=self.save_cmd)
        #Add cascade
        parent.config(menu=self.menu_bar)

    def new_cmd(self):
        pass

    def open_cmd(self):
        pass

    def save_cmd(self):
        pass

    def centre_window(self, window):
        """!
        Centre the window
        @param self The pointer for the object
        @param window The handle of the window to be centered
        """
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        window.update()
        rootsize = tuple(int(y) for y in
                         window.geometry().split('+')[0].split('x'))
        x = screen_width / 2 - rootsize[0] / 2
        y = screen_height / 2 - rootsize[1] / 2
        window.geometry("%dx%d+%d+%d" % (rootsize[0], rootsize[1], x, y))


class StdFrame(Frame):
    """!
    A class that extends the Tkinter.Frame class to provide common formatting
    """
    def __init__(self, parent, **kwargs):
        """!
        The constructor for the class
        @param self The pointer for the object
        @param parent The parent object for the frame
        @param **kwargs Other arguments as accepted by Tkinter.Frame
        """
        Frame.__init__(self, parent, **kwargs)
        self.config(background=DEFAULT_BACKGROUND)


class StdLabelFrame(LabelFrame):
    """!
    A class that extends the Tkinter.LabelFrame class to provide
    common formatting
    """
    def __init__(self, parent, **kwargs):
        """!
        The constructor for the class
        @param self The pointer for the object
        @param parent The parent object for the frame
        @param **kwargs Other arguments as accepted by Tkinter.Frame
        """
        LabelFrame.__init__(self, parent, **kwargs)
        self.configure(background=DEFAULT_BACKGROUND)


class StdLabel(Label):
    """!
    A class that extends the ttk.Label class to provide common formatting
    """
    def __init__(self, parent, **kwargs):
        """!
        The constructor for the class
        @param self The pointer for the object
        @param parent The parent object for the frame
        @param **kwargs Other arguments as accepted by ttk.Label
        """
        Label.__init__(self, parent, **kwargs)
        self.config(background=DEFAULT_BACKGROUND)


class StdEntry(Entry):
    """!
    A class that extends ttk.Entry to standardise formatting and
    functionality
    """
    def __init__(self, parent, **kwargs):
        """!
        A constructor for the class
        @param self The pointer for the object
        @param parent The parent object for the frame
        @param **kwargs Other arguments as accepted by ttk.Entry
        """
        Entry.__init__(self, parent, **kwargs)
        self.configure(background=DEFAULT_BACKGROUND)
        ##@todo Add bindings
#         self.bind('<Control-a>', self.select_all)

    def select_all(self, event):
        pass
#         print self.select_present()
#         self.select_range(0, END)
#         print self.select_present()


class StdButton(Button):
    """!
    A class that extends ttk.Button to standardise formatting and
    functionality
    """
    def __init__(self, parent, **kwargs):
        """!
        A constructor for the class
        @param self The pointer for the object
        @param parent The parent object for the frame
        @param **kwargs Other arguments as accepted by ttk.Button
        """
        #Initialise the inherited class
        Button.__init__(self, parent, **kwargs)


class StdCheckbutton(Checkbutton):
    """!
    A class that extends ttk.Checkbutton to standardise formatting
    and functionality
    """
    def __init__(self, parent, **kwargs):
            """!
            A constructor for the class
            @param self The pointer for the object
            @param parent The parent object for the frame
            @param **kwargs Other arguments as accepted by ttk.Combobox
            """
            #Initialise the inherited class
            Checkbutton.__init__(self,
                                 parent,
                                 **kwargs
                                 )
            self.config(bg=DEFAULT_BACKGROUND,
                        activebackground=DEFAULT_BACKGROUND,
                        activeforeground=DEFAULT_FOREGROUND,
                        highlightbackground=DEFAULT_BACKGROUND,
                        borderwidth=0
                        )


class StdCombobox(Combobox):
        """!
        A class that extends ttk.Combobox to standardise formatting and
        functionality
        """
        def __init__(self, parent, **kwargs):
            """!
            A constructor for the class
            @param self The pointer for the object
            @param parent The parent object for the frame
            @param **kwargs Other arguments as accepted by ttk.Combobox
            """
            #Initialise the inherited class
            Combobox.__init__(self, parent, **kwargs)


class StdScrollbar(Scrollbar):
    """!
    A class that extends the ttk.Scrollbar class to standardise formatting
    and functionality.
    """
    def __init__(self, parent, **kwargs):
        """!
        A constructor for the class
        @param self The pointer for the object
        @param parent The parent object for the frame
        @param **kwargs Other arguments as accepted by ttk.Scrollbar
        """
        #Initialise the inherited class
        Scrollbar.__init__(self, parent, **kwargs)


class StdProgressbar(Progressbar):
    """!
    A class that extends the ttk.Progressbar class to standardise formatting
    and functionality
    """
    def __init__(self, parent, **kwargs):
        """!
        A constructor for the class
        @param self The pointer for the object
        @param parent The parent object for the frame
        @param **kwargs Other arguments as accepted by ttk.Scrollbar
        """
        #Initialise the inherited class
        Progressbar.__init__(self, parent, **kwargs)


class StdTableCell(tkEntry):
    """!
    A class that extends ttk.Entry to provide a cell widget for
    tables
    """
    def __init__(self, parent, **kwargs):
        """!
        A constructor for the class
        @param self The pointer for the object
        @param parent The parent object for the frame
        @param **kwargs Other arguments as accepted by ttk.Entry
        """
        #Initialise the inherited class
        tkEntry.__init__(self, parent)
        #Apply formatting
        self.config(relief="ridge",
                    bg=DEFAULT_BACKGROUND, fg=TABLE_HEADER_TEXT_COLOUR,
                    readonlybackground=DEFAULT_BACKGROUND,
                    justify='center', width=8,
                    state="readonly")


class StdTableHeader(StdTableCell):
    """!
    A class that extends Stdtable_cell to provide a cell header widget for
    tables
    """
    def __init__(self, parent, **kwargs):
        """!
        A constructor for the class
        @param self The pointer for the object
        @param parent The parent object for the frame
        @param **kwargs Other arguments as accepted by ttk.Button
        """
        self.text = StringVar()
        self.text.set(kwargs['text'])
        StdTableCell.__init__(self, parent, **kwargs)
        self.config(bg=TABLE_HEADER_BACKGROUND, fg=TABLE_HEADER_TEXT_COLOUR,
                    readonlybackground=TABLE_HEADER_BACKGROUND,
                    textvariable=self.text)
