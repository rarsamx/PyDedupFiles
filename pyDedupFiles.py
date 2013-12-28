import sys
import os
import Tkinter
from PIL import Image, ImageTk
import logging

class Application(Tkinter.Frame):
    file_handler = None

    left_img_label = None
    left_image = None
    left_image_filename = None
    left_path_label = None

    right_img_label = None
    right_image = None
    right_image_filename = None
    right_path_label = None

    status_label = None

    del_left_btn = None
    keep_both_btn = None
    del_right_btn = None

    
    def __init__(self, master):
        Tkinter.Frame.__init__(self, master)
        self.file_handler = FileHandler("duplicates.txt")
        self.grid()
        self.create_widgets()
        self.initialize_images()

    def create_widgets(self):
        self.left_img_label = Tkinter.Label(self, relief=Tkinter.SUNKEN, justify=Tkinter.LEFT, padx=10, pady=10, text="Left side image ")
        self.left_img_label.grid(row=0, column=1, columnspan=2)
        self.right_img_label = Tkinter.Label(self, relief=Tkinter.SUNKEN, justify=Tkinter.RIGHT, padx=10, pady=10, text="Right side image ")
        self.right_img_label.grid(row=0, column=3, columnspan=2)
        self.left_path_label = Tkinter.Label(self, justify=Tkinter.LEFT, padx=10, pady=10, text="Left side path")
        self.left_path_label.grid(row=1, column=1, columnspan=2)
        self.right_path_label = Tkinter.Label(self, justify=Tkinter.RIGHT, padx=10, pady=10, text="Right side path")
        self.right_path_label.grid(row=1, column=3, columnspan=2)
        self.del_left_btn = Tkinter.Button(self, text="Delete Left", command=self.del_left_picture)
        self.del_left_btn.grid(row=2, column=1)
        self.keep_both_btn = Tkinter.Button(self, text="Keep Both", command=self.keep_both)
        self.keep_both_btn.grid(row=2, column=2, columnspan=2)
        self.del_right_btn = Tkinter.Button(self, text="Delete Right", command=self.del_right_picture)
        self.del_right_btn.grid(row=2, column=4)
        self.status_label = Tkinter.Label(self, justify=Tkinter.LEFT, padx=10, pady=10, text="Welcome to Rarsa's deduplicate")
        self.status_label.grid(row=3, column=1, columnspan=5)

    def initialize_images(self):
        image_path = self.file_handler.read_next().split("  ")[1]
        self.set_left_side_image(image_path)
        image_path = self.file_handler.read_next().split("  ")[1]
        self.set_right_side_image(image_path)
        

    def set_right_side_image(self, image_filename):
        self.right_image_filename = image_filename
        if os.path.isfile(self.right_image_filename):
            image =  Image.open(self.right_image_filename)
            image.thumbnail((640, 480), Image.ANTIALIAS)
            self.right_image = ImageTk.PhotoImage(image)
            self.right_img_label.configure(image =  self.right_image)
        else:
            self.right_img_label.configure(image = "", text =  "File Not Found")

        self.right_path_label.configure (text = self.right_image_filename)

    def set_left_side_image(self, image_filename):
        self.left_image_filename = image_filename
        if os.path.isfile(self.left_image_filename):
            image =  Image.open(self.left_image_filename)
            image.thumbnail((640, 480), Image.ANTIALIAS)
            self.left_image = ImageTk.PhotoImage(image)
            self.left_img_label.configure(image =  self.left_image)
        else:
            self.left_img_label.configure(image = "", text =  "File Not Found")

        self.left_path_label.configure (text = self.left_image_filename)

    def keep_both(self):
        self.status_label.configure (text = "Both images kept")
        self.next_image()

    def del_left_picture(self):
        self.file_handler.del_file(self.left_image_filename)
        self.status_label.configure (text = "Deleted:" + self.left_image_filename)
        self.next_image()

    def del_right_picture(self):
        self.file_handler.del_file(self.right_image_filename)
        self.status_label.configure (text = "Deleted:" + self.right_image_filename)
        self.next_image()

    def next_image(self):
        line = self.file_handler.read_next()
        if line:
            if line == "=====":
                self.initialize_images()
            else:
                image_path = line.split("  ")[1]
                self.set_right_side_image(image_path)
        else:
            self.status_label.configure (text = "End of duplicates")
            self.del_left_btn.configure (state = Tkinter.DISABLED)
            self.keep_both_btn.configure (state = Tkinter.DISABLED)
            self.del_right_btn.configure (state = Tkinter.DISABLED)

class FileHandler():
    dups_file = None

    def __init__(self, dups_filename):
        self.dups_file = open(dups_filename)
        line = self.read_next()
        if line != "=====":
            print line
            print "This is not a duplicates file or there are no duplicates"
            sys.exit(1)

    def read_next(self):
        return self.dups_file.readline().rstrip()

    def del_file(self, filename):
        os.remove(filename)
        logging.info("Deleting: %s" % filename)

    
def main():
    try:
        logging.basicConfig(filename="deduplicate.log", format='%(asctime)s %(message)s', level=logging.INFO)
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
