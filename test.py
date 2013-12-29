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
        self.grid()
        self.create_widgets()
        self.populate_lists()

    def create_widgets(self):
        self.left_img_label = Tkinter.Label(self, relief=Tkinter.SUNKEN, justify=Tkinter.LEFT, padx=10, pady=10, text="Left side image ")
        self.left_img_label.grid(row=0, column=1, columnspan=2)
        self.right_img_label = Tkinter.Label(self, relief=Tkinter.SUNKEN, justify=Tkinter.RIGHT, padx=10, pady=10, text="Right side image ")
        self.right_img_label.grid(row=0, column=3, columnspan=2)
        self.left_path_label = Tkinter.Label(self, justify=Tkinter.LEFT, padx=10, pady=10, text="Left side path")
        self.left_path_label.grid(row=1, column=1, columnspan=2)
        self.right_path_label = Tkinter.Label(self, justify=Tkinter.RIGHT, padx=10, pady=10, text="Right side path")
        self.right_path_label.grid(row=1, column=3, columnspan=2)
        self.del_left_btn = Tkinter.Button(self, text="Delete Left")
        self.del_left_btn.grid(row=2, column=1)
        self.keep_both_btn = Tkinter.Button(self, text="Keep Both")
        self.keep_both_btn.grid(row=2, column=2, columnspan=2)
        self.del_right_btn = Tkinter.Button(self, text="Delete Right")
        self.del_right_btn.grid(row=2, column=4)
        
        self.left_list = Tkinter.Listbox(self)
        self.left_list.grid(row=3, column=1, columnspan=2)
        self.left_list.bind("<Double-Button-1>", self.OnDouble)
        self.right_list = Tkinter.Listbox(self)
        self.right_list.grid(row=3, column=3, columnspan=2)
                
        self.status_label = Tkinter.Label(self, justify=Tkinter.LEFT, padx=10, pady=10, text="Welcome to Rarsa's deduplicate")
        self.status_label.grid(row=4, column=1, columnspan=5)
    
    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        print "selection:", selection, ": '%s'" % value
    
    def populate_lists(self):
        directoryListing = os.listdir("/home/henriquen/Pictures")
        for filename in sorted(directoryListing):
            if os.path.isdir(os.path.join("/home/henriquen/Pictures",filename)):
                self.left_list.insert(Tkinter.END, filename)
                self.right_list.insert(Tkinter.END, filename)
      
def main():
    try:
        logging.basicConfig(filename="samplelist.log", format='%(asctime)s %(message)s', level=logging.DEBUG)
        logging.info("Starting")
        root = Tkinter.Tk()
        root.title("Show list of files")
        
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
