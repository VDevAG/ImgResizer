from PIL import Image
import os
import sys
import imghdr
from tkinter import Button, Label, Grid, Tk, Entry, StringVar
from tkinter import ttk
from tkinter import filedialog


directory = os.listdir(os.getcwd())


class Resizer:
    def __init__(self, input_directory, output_directory, size, name_add_on):
        self.dir = input_directory
        self.input_directory = os.listdir(input_directory)
        self.output_directory = output_directory
        self.size = size
        self.name_add_on = name_add_on

    def _control_image(self, file):
        if imghdr.what(self.dir + "/" + str(file)) == None:
            print("false")
            return False
        else:
            print("true")
            return True


    def resize_all(self):
        print(self.input_directory)
        for item in self.input_directory:
            print("görs detta??")
            if self._control_image(item):
                print("här")
                fp = self.dir + "/" + str(item)
                im = Image.open(fp)
                f, e = os.path.splitext(fp)
                im_resize = im.resize(self.size, Image.ANTIALIAS)
                im_resize.save(self.output_directory + "/" + item, 'JPEG', quality=90)

class Gui:
    def __init__(self):
        gui = Tk()
        gui.geometry("500x200")
        gui.title("Image resizer")

        def get_input_path():
            folder_selected = filedialog.askdirectory()
            input_path.set(folder_selected)

        def get_output_path():
            folder_selected = filedialog.askdirectory()
            output_path.set(folder_selected)

        def resize_images():
            inputp = input_path.get()
            outputp = output_path.get()
            r = Resizer(inputp, outputp, (200, 200), "resized.jpeg")
            r.resize_all()

        input_path = StringVar()
        output_path = StringVar()

        input_label = Label(gui ,text="Specify Input path")
        input_label.grid(row=0,column = 0)
        input_entry = Entry(gui,textvariable=input_path)
        input_entry.grid(row=0,column=1)
        btn_find = ttk.Button(gui, text="Browse Folder",command=get_input_path)
        btn_find.grid(row=0,column=2)

        output_label = Label(gui ,text="Specify Output path")
        output_label.grid(row=1,column = 0)
        ouput_entry = Entry(gui,textvariable=output_path)
        ouput_entry.grid(row=1,column=1)
        btn_find = ttk.Button(gui, text="Browse Folder",command=get_output_path)
        btn_find.grid(row=1,column=2)

        button = ttk.Button(gui ,text="Resize images", command=resize_images)
        button.grid(row=3,column=0)
        gui.mainloop()

app = Gui()

