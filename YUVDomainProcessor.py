# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 20:51:14 2021

@author: qilin
"""
import numpy as np




# Step Luma-2. 'Edge Enhancement'
class EdgeEnhancement:
    def __init__(self, img, edge_filter, gain, thres, emclip):
        self.img = img
        self.edge_filter = edge_filter
        self.gain = gain
        self.thres = thres
        self.emclip = emclip

    def padding(self):
        img_pad = np.pad(self.img, ((1, 1), (2, 2)), 'reflect')
        return img_pad

    def clipping(self):
        np.clip(self.img, 0, 255, out=self.img)
        return self.img

    def emlut(self, val, thres, gain, clip):  # Edge map look up table
        lut = 0
        # Your code here 
        return lut

    def execute(self):
        img_pad = self.padding()
        img_h = self.img.shape[0]
        img_w = self.img.shape[1]
        ee_img = np.empty((img_h, img_w), np.int16)
        em_img = np.empty((img_h, img_w), np.int16)
       # Your code here 

        return  

# Step Luma-3. 'Brightness Contrast Control'
class BrightnessContrastControl: 
    def __init__(self, img, brightness, contrast, clip):
        self.img = img
        self.brightness = brightness
        self.contrast = contrast
        self.clip = clip

    def clipping(self):
        np.clip(self.img, 0, self.clip, out=self.img)
        return self.img

    def execute(self):
        img_h = self.img.shape[0]
        img_w = self.img.shape[1]
        # Your code here 

        return  



# Step Chroma-1 False Color Suppression
class FalseColorSuppression:
    def __init__(self, img, edgemap, fcs_edge, gain, intercept, slope):
        self.img = img
        self.edgemap = edgemap
        self.fcs_edge = fcs_edge
        self.gain = gain
        self.intercept = intercept
        self.slope = slope

    def clipping(self):
        # Your code here 

        return  

    def execute(self):
        img_h = self.img.shape[0]
        img_w = self.img.shape[1]
        img_c = self.img.shape[2]
        # Your code here 

        return  
    
# Step Chroma-2 Hue/Saturation control
class HueSaturationControl:
    def __init__(self, img, hue, saturation, clip):
        self.img = img
        self.hue = hue
        self.saturation = saturation
        self.clip = clip

    def clipping(self):
        np.clip(self.img, 0, self.clip, out=self.img)
        return self.img

    def lut(self):
        ind = np.array([i for i in range(360)])
        sin = np.sin(ind * np.pi / 180) * 256
        cos = np.cos(ind * np.pi / 180) * 256
        lut_sin = dict(zip(ind, [round(sin[i]) for i in ind]))
        lut_cos = dict(zip(ind, [round(cos[i]) for i in ind]))
        return lut_sin, lut_cos

    def execute(self):
        lut_sin, lut_cos = self.lut()
        img_h = self.img.shape[0]
        img_w = self.img.shape[1]
        img_c = self.img.shape[2]
        # Your code here 
        
        return  