from PIL import Image, ImageDraw, ImageEnhance
from PyQt5 import QtGui, QtCore, QtWidgets
import os
import requests

from ..component import Component
from ..toolkit.frame import BlankFrame
import tempfile
import urllib.request 

class Component(Component):
    name = 'Unsplash Image'
    version = '1.0.0'

    

    def widget(self, *args):
        print("creating");
        super().widget(*args)
        print("tracking")

        self.page.lineedit_tags.setText("landscape,purple")
        self.trackWidgets({
            '_tags': self.page.lineedit_tags,
        })

        def getImage():
            url = "https://source.unsplash.com/random/" + str(self.width) + "x" + str(self.height) + "?" + str(self._tags)
            #r = requests.get(url) 
            #print(url)
            #print(r.url)
            urllib.request.urlretrieve(url, tempfile.gettempdir() + "/unsplash_tmp.png")
            print("uwu!!");
        getImage();
        self.page.button_new.clicked.connect(getImage)
        
        print("created")

    def previewRender(self):
        return self.drawFrame(self.width, self.height)

    def properties(self):
        props = ['static']
        return props

    def frameRender(self, frameNo):
        return self.drawFrame(self.width, self.height)

    def drawFrame(self, width, height):
        frame = BlankFrame(width, height)
        if tempfile.gettempdir() + "/unsplash_tmp.png" and os.path.exists(tempfile.gettempdir() + "/unsplash_tmp.png"):
            image = Image.open(tempfile.gettempdir() + "/unsplash_tmp.png")
            image = image.resize((self.width, self.height), Image.ANTIALIAS)
            frame.paste(image, box=(0, 0))

        return frame

    def savePreset(self):
        # what the fuck
        return super().savePreset()

    def update(self):
        # i dont know what this does
        return
