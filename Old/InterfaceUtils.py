import ctypes
import threading
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk

#---------------------------------------------------------------------------------------------

def progressBarSet(index, qItens, title):
    
    total = int(qItens / 5)
    complete = int(index / 5)
    rest = total - complete

    value = "     " + '='*complete + '_'*rest + " \n" + "     " + str(index) + "%"
    ctypes.windll.user32.MessageBoxW(0, value, title, 0)

#---------------------------------------------------------------------------------------------

def progressBar (current = 0):

    t = threading.Thread(target=progressBarSet, args=(current, 100,"Progress", ))
    t.start()

#---------------------------------------------------------------------------------------------

def progressBarUpdate(current): 

    progressBarClose("Progress")
    progressBar (current)

#---------------------------------------------------------------------------------------------

def progressBarClose(title):

    wd=ctypes.windll.user32.FindWindowW(0,title)
    ctypes.windll.user32.SendMessageW(wd,0x0010,0,0)

#---------------------------------------------------------------------------------------------

def messageBox (title, message, icon = 0x10, buttons = 0, styleWindow = 0x2000):

    # ICON
    #MB_ICONEXCLAMATION = MB_ICONWARNING = 0x30
    #MB_ICONINFORMATION = MB_ICONASTERISK = 0x40
    #MB_ICONQUESTION = 0x20
    #MB_ICONSTOP = MB_ICONERROR = MB_ICONHAND = 0x10

    #BUTTONS
    #MB_ABORTRETRYIGNORE = 2
    #MB_CANCELTRYCONTINUE = 6
    #MB_HELP = 0x4000
    #MB_OK = 0
    #MB_OKCANCEL = 1
    #MB_RETRYCANCEL = 5
    #MB_YESNO = 4
    #MB_YESNOCANCEL = 3

    #STYLE WINDOW
    #MB_APPLMODAL = 0
    #MB_SYSTEMMODAL = 0x1000
    #MB_TASKMODAL = 0x2000

    return ctypes.windll.user32.MessageBoxW(None, message, title, icon | buttons | styleWindow)

#---------------------------------------------------------------------------------------------
class ProgressBar( tk.Toplevel ):

    start = value = 0
    end = 1
    label_text = ''

    def __init__(self, start=0, end=1, *, label_text=None, parent=None):

        self._parent = None     
        self.start = self.value = start
        self.end = end

        if (label_text is None):
            label_text = ''

        if parent == None:
            parent = tk.Tk()
            parent.withdraw()

        super(ProgressBar, self).__init__(parent)

        self.title("") # window title.

        settings = dict()
        settings['text'] = ''
        settings['justify'] = tk.LEFT
        settings['anchor'] = tk.W

        self._label = tk.Label(self, **settings)
        self._label.pack(fill=tk.BOTH, expand=True)
        self._label_pack_info = self._label.pack_info() # save label place.

        self.setLabel(label_text)

        settings = dict()
        settings['orient'] = tk.HORIZONTAL
        settings['mode'] = 'determinate'
        settings['length'] = 300
        settings['value'] = 0

        self._main = ttk.Progressbar(self, **settings)
        self._main.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

        self.setRange(start, end)

        # include label.
        self._style = ttk.Style(self)
        self._style.layout('text.Horizontal.TProgressbar',
                           [('Horizontal.Progressbar.trough',
                             { 'children' :  [('Horizontal.Progressbar.pbar',
                                              { 'side'   : 'left', 
                                                'sticky' : 'ns' })],
                              'sticky'    : 'nswe' }),
                            ('Horizontal.Progressbar.label', 
                             { 'sticky' : '' })
                           ])
        self._style.configure('text.Horizontal.TProgressbar', text=f'0 / {end - start}')
        self._main['style'] = 'text.Horizontal.TProgressbar'

        self.wm_attributes('-topmost', 1) # keeps window always on top.
        self.attributes('-toolwindow', 1) # remove minimize and maximize buttons.
        self.resizable(width=False, height=False)
        self.wm_protocol('WM_DELETE_WINDOW', self.cancel)
        self.focus() # give focus to root window.

        self.update()

        # get screen width and height.
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()

        width = self.winfo_width()
        height = self.winfo_height()

        # calculate position x, y.
        x = (ws/2) - (width/2)
        y = (hs/2) - (height/2)

        self.geometry(f'{int(width)}x{int(height)}+{int(x)}+{int(y)}') # center widget in screen.

        self.update()


    def exit(self):

        if self.is_active():
            self.update()
            self.destroy()
            if (self._parent is not None) and (len(self._parent.children) == 0):
                self._parent.quit()


    def cancel(self, event=None):

        self.exit()


    def setLabel(self, value):

        if self.is_active():

            self._label['text'] = value
            
            if (value == ''):
                self._label.pack_forget()
            else:
                self._label.pack(self._label_pack_info)


    def setRange(self, start, end):

        if self.is_active():

            self.start = self.value = start
            self.end = end

            self._main['maximum'] = end - start


    def setValue(self, value):

        if self.is_active():

            value = max(self.start,  min(value, self.end))

            if (value > self.value):
                self._main['value'] = value - self.start
                self._style.configure('text.Horizontal.TProgressbar', text=f'{self._main["value"]} / {self._main["maximum"]}')
                self.update()

                self.value = value


    def step(self, amount=1):

        if self.is_active():

            amount = min(amount, self.end - self.value)

            if (amount > 0):
                self._main['value'] += amount
                self._style.configure('text.Horizontal.TProgressbar', text=f'{self._main["value"]} / {self._main["maximum"]}')
                self.update()

                self.value += amount


    def stop(self, label_text=None):

        if self.is_active():

            if (label_text is not None):
                self.setLabel(label_text)
            self.setValue(self.end)
            time.sleep(2) # wait for 2 seconds.

            self.exit()


    def reset(self, label_text=None):

        if self.is_active():

            if (label_text is not None):
                self.setLabel(label_text)

            self._main['value'] = 0
            self._style.configure('text.Horizontal.TProgressbar', text=f'{self._main["value"]} / {self._main["maximum"]}')
            self.update()

            self.value = 0


    def is_active(self):

        return self.winfo_exists()
    
    
class progressBarWithChecks():
    
    def __init__(self, listChecks, title, total= 100):
        
        self.root= None
        self.listChecks= listChecks
        self.title= title
        self.style= None
        
        self.value= 0
        self.total = total
        
        self.progressBarHeight= 25 
        self.checksHeight= 30
        self.totalHeight= self.checksHeight*(len(self.listChecks) + 1) + self.progressBarHeight + 10
        
        self.checkVars= {}
        self.progressBarVar= None    
        self.progressBar= None
               
        self.interface()
        self.styleProgressbar()
        
    def interface(self):
        
        self.root= Tk()
        self.root.title(self.title)
        self.root.geometry("250x" + str(self.totalHeight))
        self.root.resizable(width= False, height= False)
        
        self.progressBarVar= tk.DoubleVar() 
        self.progressBar= ttk.Progressbar(self.root, length= 200, variable= self.progressBarVar)
        self.progressBar.place(x=25, y= 20, height= self.progressBarHeight)
        self.progressBar['maximum']= self.total

        for checkItem in self.listChecks:
            
            self.checkVars[checkItem]= tk.BooleanVar()
            
            cb= Checkbutton(self.root, text=checkItem, variable=self.checkVars[checkItem], state= DISABLED)
            cb.place(x=25, y= self.listChecks.index(checkItem)*self.checksHeight + 50, width= 200, height=30)
            
    def show(self):
        
        threading.Thread(target=self.root.mainloop).start()
        
    def setValue(self, value):
        
        self.value= value
        self.progressBarVar.set(self.value)
        self.style.configure('text.Horizontal.TProgressbar', text=f'{self.value} / {self.total}')
        self.root.update()
                
    def setIcon (self, pathImage):
        
        self.root.iconphoto(False, PhotoImage(file = pathImage))
        
    def styleProgressbar(self):
        
        self.style= ttk.Style(self.root)
        
        self.style.layout('text.Horizontal.TProgressbar',
                           [('Horizontal.Progressbar.trough',
                             { 'children' :  [('Horizontal.Progressbar.pbar',
                                              { 'side'   : 'left', 
                                                'sticky' : 'ns' })],
                              'sticky'    : 'nswe' }),
                            ('Horizontal.Progressbar.label', 
                             { 'sticky' : '' })
                           ])
        
        self.style.configure('text.Horizontal.TProgressbar', text=f'0 / {self.total}')
        
        self.progressBar['style']= 'text.Horizontal.TProgressbar'
        self.root.update()
        
    def checkItem(self, item):
        
        self.checkVars[item].set(True)
        