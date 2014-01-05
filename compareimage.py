from PIL import Image, ImageTk
import math, operator
import sys
import os
import progress


class CompImage():
    filename = None
    img = None
    h = None
    
    def __init__(self, filename):
        self.filename = filename
        
    def set_h(self):
        try:
            self.img=Image.open(self.filename)
            self.img.thumbnail((128, 128), Image.ANTIALIAS)
            self.h = self.img.histogram()
        except:
            self.img = None
            self.h = None

        
def compare(compImg1, compImg2, threshold):
    h1 = compImg1.h
    h2 = compImg2.h

    rms = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
    print rms
    return rms < threshold


#compImg1 = CompImage(sys.argv[1])
#compImg2 = CompImage(sys.argv[2])

allfiles = []
for root, dirs, files in os.walk(sys.argv[1]):
    for name in files:
        if os.path.splitext(name)[1].lower() == '.jpg'.lower():
            fullpath = os.path.join(root,name)
            compImg = CompImage(fullpath)
            allfiles.append(compImg)

pb = progress.ProgressBar(len(allfiles), 'Image files')

for compImg in allfiles:
    compImg.set_h()
    pb.increment()


#print compare(compImg1, compImg2, 40)

    
    

