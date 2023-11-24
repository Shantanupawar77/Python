import numpy as np
import imageio
import scipy.ndimage
import cv2
img="sss7.jpeg"


def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])

def dodge(front,back):
    final_skech=front*255/(255-back)
    final_skech[final_skech>255]=255
    return final_skech.astype('uint8')

ss=imageio.imread(img)
gray=rgb2gray(ss)
i=255-gray
blur=scipy.ndimage.filters.gaussian_filter(i,sigma=15)
r=dodge(blur,gray)
cv2.imwrite("sss7_new.jpeg",r)