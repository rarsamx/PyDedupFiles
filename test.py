import sys
import os
import Tkinter
from PIL import Image, ImageTk
import logging

class Application(Tkinter.Frame):
    left_img_label = None
    left_path_label = None
    left_list = None

    right_img_label = None
    right_path_label = None
    right_list = None

    status_label = None

    del_left_btn = None
    keep_both_btn = None
    del_right_btn = None
    
    def __init__(self, master):
        Tkinter.Frame.__init__(self, master)
        self.grid(sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        for column in range(4):
            self.columnconfigure(column, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)
        self.create_widgets()
        self.populate_lists()

    def create_widgets(self):
        self.left_img_label = Tkinter.Label(self, relief=Tkinter.SUNKEN, justify=Tkinter.LEFT, padx=10, pady=10, text="Left side image ")
        self.left_img_label.grid(row=0, column=0, columnspan=2, sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.right_img_label = Tkinter.Label(self, relief=Tkinter.SUNKEN, justify=Tkinter.RIGHT, padx=10, pady=10, text="Right side image ")
        self.right_img_label.grid(row=0, column=2, columnspan=2, sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.left_path_label = Tkinter.Label(self, justify=Tkinter.LEFT, padx=10, pady=10, text="Left side path")
        self.left_path_label.grid(row=1, column=0, columnspan=2)
        self.right_path_label = Tkinter.Label(self, justify=Tkinter.RIGHT, padx=10, pady=10, text="Right side path")
        self.right_path_label.grid(row=1, column=2, columnspan=2)
        self.del_left_btn = Tkinter.Button(self, text="Delete Left")
        self.del_left_btn.grid(row=2, column=0)
        self.keep_both_btn = Tkinter.Button(self, text="Keep Both")
        self.keep_both_btn.grid(row=2, column=1, columnspan=2)
        self.del_right_btn = Tkinter.Button(self, text="Delete Right")
        self.del_right_btn.grid(row=2, column=3)
        
        left_frame = Tkinter.Frame(self)
        left_frame.grid(row=3, column=0, columnspan=2, sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        left_frame.columnconfigure(0, weight=1)
        left_frame.rowconfigure(0, weight=1)

        self.left_list = Tkinter.Listbox(left_frame)
        self.left_list.grid(row=0, column=0, columnspan=1, sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.left_list.bind("<Double-Button-1>", self.OnDouble)
        self.left_list.bind("<Configure>", self.OnResize)
        yscroll = Tkinter.Scrollbar(left_frame, command=self.left_list.yview, orient=Tkinter.VERTICAL)
        yscroll.grid(row=0, column=1, sticky=Tkinter.N+Tkinter.S)
        self.left_list.configure(yscrollcommand=yscroll.set)
        
        right_frame = Tkinter.Frame(self)
        right_frame.grid(row=3, column=2, columnspan=2, sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        right_frame.columnconfigure(0, weight=1)
        right_frame.rowconfigure(0, weight=1)

        self.right_list = Tkinter.Listbox(right_frame)
        self.right_list.grid(row=0, column=0, sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.right_list.bind("<Double-Button-1>", self.OnDouble)
        yscroll2 = Tkinter.Scrollbar(right_frame, command=self.right_list.yview, orient=Tkinter.VERTICAL)
        yscroll2.grid(row=0, column=1, sticky=Tkinter.N+Tkinter.S)
        self.right_list.configure(yscrollcommand=yscroll2.set)
                
        self.status_label = Tkinter.Label(self, justify=Tkinter.LEFT, padx=10, pady=10, text="Welcome to Rarsa's deduplicate")
        self.status_label.grid(row=4, column=0, columnspan=5)
    
    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        print "selection:", selection, ": '%s'" % value
    
    def OnResize(self, event):
        widget = event.widget
        print "new size (%d, %d):" % (event.width, event.height)
    
    def populate_lists(self):
        folder = "/media/Data/Fotos"
        directoryListing = os.listdir(folder)
        for filename in sorted(directoryListing):
            if os.path.isdir(os.path.join(folder,filename)):
                self.left_list.insert(Tkinter.END, filename)
                self.right_list.insert(Tkinter.END, filename)
      
def main():
    try:
        logging.basicConfig(filename="test.log", format='%(asctime)s %(message)s', level=logging.DEBUG)
        logging.info("Starting")
        root = Tkinter.Tk()
        root.title("Show list of files")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        app = Application(root)

        if "idlelib" not in sys.modules:
            root.mainloop()
    except:
        logging.exception("")
        raise
    finally:
        logging.info("Ending")


if __name__ == "__main__":
    main()
