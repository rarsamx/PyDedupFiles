import sys
import os
import Tkinter
from PIL import Image, ImageTk
import logging

class Application(Tkinter.Frame):
    file_handler = None

    left_img_frame = None
    right_img_frame = None

    del_left_btn = None
    keep_both_btn = None
    del_right_btn = None

    status_label = None
    
    def __init__(self, master):
        Tkinter.Frame.__init__(self, master)
        self.file_handler = FileHandler("duplicates.txt")
        self.grid()
        self.create_widgets()
        self.next_image()

    def create_widgets(self):
        self.left_img_frame = ImageFrame(self)
        self.left_img_frame.grid(row=0, column=0, columnspan=2)
        self.right_img_frame = ImageFrame(self)
        self.right_img_frame.grid(row=0, column=2, columnspan=2)

        self.del_left_btn = Tkinter.Button(self, text="Delete Left", command=self.del_left_picture)
        self.del_left_btn.grid(row=2, column=0)
        self.keep_both_btn = Tkinter.Button(self, text="Keep Both", command=self.keep_both)
        self.keep_both_btn.grid(row=2, column=1, columnspan=2)
        self.del_right_btn = Tkinter.Button(self, text="Delete Right", command=self.del_right_picture)
        self.del_right_btn.grid(row=2, column=3)
        self.status_label = Tkinter.Label(self, justify=Tkinter.LEFT, padx=10, pady=10, text="Welcome to Rarsa's deduplicate")
        self.status_label.grid(row=3, column=0, columnspan=5)
      
    def next_image(self):
        logging.debug("next_image")
        line = self.file_handler.read_next()
        while line and not (self.left_img_frame.is_image_set() and self.right_img_frame.is_image_set()):
            if line == "=====":
                logging.debug("reset")
                self.left_img_frame.reset_image()
                self.right_img_frame.reset_image()
            else:
                image_path = line.split("  ")[1]
                if os.path.isfile(image_path):
                    if not self.left_img_frame.is_image_set():
                        logging.debug("Setting Left Image: %s" % image_path)
                        self.left_img_frame.set_image(image_path)
                    else:
                        logging.debug("Setting Right Image: %s" % image_path)
                        self.right_img_frame.set_image(image_path)
            if not self.right_img_frame.is_image_set():
                line = self.file_handler.read_next()
                        
        if self.left_img_frame.is_image_set() and self.right_img_frame.is_image_set():
            self.left_img_frame.display_image()
            self.right_img_frame.display_image()
        else:            
            self.status_label.configure (text = "End of duplicates")
            self.del_left_btn.configure (state = Tkinter.DISABLED)
            self.keep_both_btn.configure (state = Tkinter.DISABLED)
            self.del_right_btn.configure (state = Tkinter.DISABLED)
            self.left_img_frame.reset_image()
            self.right_img_frame.reset_image()

    def keep_both(self):
        logging.debug("Both images kept")
        self.status_label.configure (text = "Both images kept")
        self.right_img_frame.reset_image()
        self.next_image()

    def del_left_picture(self):
        self.file_handler.del_file(self.left_img_frame.image_filename)
        logging.debug("Deleted left image")
        self.status_label.configure (text = "Deleted left image")
        self.left_img_frame.set_image(self.right_img_frame.image_filename)
        self.right_img_frame.reset_image()
        self.next_image()

    def del_right_picture(self):
        self.file_handler.del_file(self.right_img_frame.image_filename)
        logging.debug("Deleted right image")
        self.status_label.configure (text = "Deleted right image")
        self.right_img_frame.reset_image()
        self.next_image()

class ImageFrame(Tkinter.Frame):
    image = None
    image_filename = None
    
    img_label = None
    path_label = None

    def __init__(self, master):
        Tkinter.Frame.__init__(self, master)
        self.create_widgets()
        
    def create_widgets(self):
        self.img_label = Tkinter.Label(self, relief=Tkinter.SUNKEN, justify=Tkinter.LEFT, padx=10, pady=10)
        self.img_label.grid(row=0, column=1)
        self.path_label = Tkinter.Label(self, justify=Tkinter.LEFT, padx=10, pady=10)
        self.path_label.grid(row=1, column=1)

    def reset_image(self):
        self.image = None
        self.image_filename = None
        self.img_label.configure(image =  None)
        self.path_label.configure (text = "")
        
    def is_image_set(self):
        return self.image_filename != None
        
    def set_image(self, image_filename):
        self.image_filename = image_filename
        
    def display_image(self):
        self.path_label.configure (text = self.image_filename)
        image_file =  Image.open(self.image_filename)
        image_file.thumbnail((640, 480), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(image_file)
        self.img_label.configure(image =  self.image)

class FileHandler():
    dups_file = None

    def __init__(self, dups_filename):
        self.dups_file = open(dups_filename)

    def read_next(self):
        return self.dups_file.readline().rstrip()

    def del_file(self, filename):
        logging.info("Deleting: %s" % filename)
        os.remove(filename)

    
def main():
    try:
        logging.basicConfig(filename="deduplicate.log", format='%(asctime)s %(message)s', level=logging.DEBUG)
        logging.info("Starting")
        root = Tkinter.Tk()
        root.title("Deduplicate images")
        
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
