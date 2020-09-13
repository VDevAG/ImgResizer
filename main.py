from PIL import Image
import os, sys

dirs = os.listdir(os.getcwd())
def resize():
        print("test")
        print(os.path.join(os.path.dirname(__file__)))
        for item in dirs:
            if os.path.isfile(item) and str(item).endswith("g") and not  "resized" in str(item):
                im = Image.open(item)
                f, e = os.path.splitext(item)
                imResize = im.resize((200,200), Image.ANTIALIAS)
                imResize.save(f + ' resized.jpg', 'JPEG', quality=90)
resize()
