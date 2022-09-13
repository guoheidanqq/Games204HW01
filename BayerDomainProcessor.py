# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 19:45:23 2021

@author: qilin sun
"""
import numpy as np


# For this file, use numpy only.  Try your best to get the best visual pleasent
# result, as well as the fasest speed and smallest memory consumption.

# Step 1. Dead Pixel Correction (10pts)
class deadPixelCorrection:

    def __init__(self, img, thres, mode, clip):
        self.img = img
        self.thres = thres
        self.mode = mode
        self.clip = clip

    def padding(self):
        # padding needed for avoid black boundry
        # Fill your code here
        # TODO padding  ignore first
        return

    def clipping(self):
        # clip needed for avoid values>maximum
        # Fill your code here
        self.img = np.clip(self.img, 0, self.clip)
        return

    def get_p1(self, i, j):
        if self.is_in_boundary(i, j):
            return self.img[i - 2, j - 2]
        else:
            return self.get_outside()

    def get_p2(self, i, j):
        if self.is_in_boundary(i, j):
            return self.img[i - 2, j]
        else:
            return self.get_outside()

    def get_p3(self, i, j):
        if self.is_in_boundary(i, j):
            return self.img[i - 2, j + 2]
        else:
            return self.get_outside()

    def get_p4(self, i, j):
        if self.is_in_boundary(i, j):
            return self.img[i, j - 2]
        else:
            return self.get_outside()

    def get_p5(self, i, j):
        if self.is_in_boundary(i, j):
            return self.img[i, j + 2]
        else:
            return self.get_outside()

    def get_p6(self, i, j):
        if self.is_in_boundary(i, j):
            return self.img[i + 2, j - 2]
        else:
            return self.get_outside()

    def get_p7(self, i, j):
        if self.is_in_boundary(i, j):
            return self.img[i + 2, j]
        else:
            return self.get_outside()

    def get_p8(self, i, j):
        if self.is_in_boundary(i, j):
            return self.img[i + 2, j + 2]
        else:
            return self.get_outside()

    def is_in_boundary(self, i, j):
        if i - 2 < 0 or i + 2 > self.img.shape[0] - 1 or j - 2 < 0 or j + 2 > self.img.shape[1] - 1:
            return False
        else:
            return True

    def get_outside(self):
        OUTSIDE_VALUE = 0
        return OUTSIDE_VALUE

    def execute(self):
        # Fill your code here
        self.clipping()

        dpc_img = self.img
        # TODO color R
        WIDTH = self.img.shape[0]
        HEIGHT = self.img.shape[1]
        count = 0
        for i in range(0, WIDTH):
            for j in range(0, HEIGHT):
                p0 = self.img[i, j]
                p1 = self.get_p1(i, j)
                p2 = self.get_p2(i, j)
                p3 = self.get_p3(i, j)
                p4 = self.get_p4(i, j)
                p5 = self.get_p5(i, j)
                p6 = self.get_p6(i, j)
                p7 = self.get_p7(i, j)
                p8 = self.get_p8(i, j)
                if np.all(abs(np.array([p1, p2, p3, p4, p5, p6, p7, p8]) - p0) > self.thres):
                    # print("dead pixel: " + str(i) + " " + str(j))
                    count = count + 1
                    print(count)
        print(count)
        return dpc_img
        # return 1


# Step 2.'Black Level Compensation'   (10pts)
class blackLevelCompensation:
    def __init__(self, img, parameter, bayer_pattern='rggb', clip=255):
        self.img = img
        self.parameter = parameter
        self.bayer_pattern = bayer_pattern
        self.clip = clip

    def clipping(self):
        # clip needed for avoid values>maximum, find a proper value for 14bit raw input
        # Fill your code here

        return

    def execute(self):
        bl_r = -self.parameter[0]
        bl_gr = -self.parameter[1]
        bl_gb = -self.parameter[2]
        bl_b = -self.parameter[3]
        alpha = self.parameter[4]
        beta = self.parameter[5]
        # Fill your code here

        return

    # Step 3.'lens shading correction


# Skip this step

# Step 4. Anti Aliasing Filter (10pts)
class antiAliasingFilter:
    'Anti-aliasing Filter'

    def __init__(self, img):
        self.img = img

    def padding(self):
        # padding needed for avoid black boundry
        # Fill your code here

        return
        # Hint: "In bayer domain, the each ,R,G,G,B pixel is skipped by 2."

    def execute(self):
        # Fill your code here

        return


# Step 5. Auto White Balance and Gain Control (10pts)
class AWB:
    def __init__(self, img, parameter, bayer_pattern, clip):
        self.img = img
        self.parameter = parameter
        self.bayer_pattern = bayer_pattern
        self.clip = clip

    def clipping(self):
        # clip needed for avoid values>maximum, find a proper value for 14bit raw input
        # Fill your code here

        return

    def execute(self):
        # calculate Gr_avg/R_avg, 1, Gr_avg/Gb_avg, Gr_avg/B_avg and apply to each channel
        # Fill your code here

        return

    # Step 6. Chroma Noise Reduction (Additional 20pts)


# Ref: https://patentimages.storage.googleapis.com/a8/b7/82/ef9d61314d91f6/US20120237124A1.pdf

class ChromaNoiseFiltering:
    def __init__(self, img, bayer_pattern, thres, gain, clip):
        self.img = img
        self.bayer_pattern = bayer_pattern
        self.thres = thres
        self.gain = gain
        self.clip = clip

    def padding(self):
        # Fill your code here

        return

    def clipping(self):
        # Fill your code here

        return

    def cnc(self, is_color, center, avgG, avgC1, avgC2):
        'Chroma Noise Correction'
        r_gain, gr_gain, gb_gain, b_gain = self.gain[0], self.gain[1], self.gain[2], self.gain[3]
        dampFactor = 1.0
        signalGap = center - max(avgG, avgC2)
        # Fill your code here

        return

    def cnd(self, y, x, img):
        'Chroma Noise Detection'
        avgG = 0
        avgC1 = 0
        avgC2 = 0
        is_noise = 0
        # Fill your code here

        return is_noise, avgG, avgC1, avgC2

    def cnf(self, is_color, y, x, img):
        is_noise, avgG, avgC1, avgC2 = self.cnd(y, x, img)
        # Fill your code here

        return

    def execute(self):
        # Fill your code here

        return

    # Step 7. 'Color Filter Array Interpolation'  with Malvar Algorithm ”High Quality Linear“ (20pts)


class CFA_Interpolation:
    def __init__(self, img, mode, bayer_pattern, clip):
        self.img = img
        self.mode = mode
        self.bayer_pattern = bayer_pattern
        self.clip = clip

    def padding(self):
        # Fill your code here

        return

    def clipping(self):
        # Fill your code here

        return

    # def malvar(self, is_color, center, y, x, img):
    # Fill your code here

    # return [r, g, b]

    def execute(self):
        img_pad = self.padding()
        img_pad = img_pad.astype(np.int32)
        raw_h = self.img.shape[0]
        raw_w = self.img.shape[1]
        cfa_img = np.empty((raw_h, raw_w, 3), np.int16)
        # Fill your code here

        return
