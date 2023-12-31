# -*- coding: utf-8 -*-
"""Assigment_2_Q1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aVRKThJZbqkqcSPCG0HfOhMG_xwzNeiC
"""

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

im = cv.imread('the_berry_farms_sunflower_field.jpeg', cv.IMREAD_REDUCED_COLOR_4)
im = cv.cvtColor(im, cv.COLOR_BGR2RGB)
#plot image
plt.imshow(im)


im_gray = cv.cvtColor(im, cv.COLOR_RGB2GRAY)
K = np.arange(1,11,0.25)
for k in K:
    im_ = im.copy()
    scale_space = np.empty((im.shape[0] ,im.shape[1] , 500), dtype=np.float64)
    sigmas = np.arange(k,k+0.5, 0.01)
    for i, sigma in enumerate(sigmas):
        log_hw = 3*np.ceil(np.max(sigmas))
        X, Y = np.meshgrid(np.arange(-log_hw, log_hw + 1, 1), np.arange(-log_hw, log_hw + 1, 1))
        log = 1/(2*np.pi*sigma**2)*(X**2/(sigma**2) + Y**2/(sigma**2) - 2)*np.exp(-(X**2 + Y**2)/(2*sigma**2))
        f_log = cv.filter2D(im_gray, cv.CV_64F, log)
        scale_space[:, :, i] = f_log

    indices = np.unravel_index(np.argmax(scale_space, axis=None), scale_space.shape)
    r = sigmas[indices[2]]*np.sqrt(2)

    #draw a circle around the detected blob
    cv.circle(im_, (int(indices[1]), int(indices[0])), int(r), (0,255,0), 2)
    fig, ax = plt.subplots()
    plt.title('r = ' + str(r) + ', sigma = ' + str(sigmas[indices[2]]))
    plt.imshow(im_)


im_gray = cv.cvtColor(im, cv.COLOR_RGB2GRAY)
K = np.arange(1,11,0.125)
for k in K:
    scale_space = np.empty((im.shape[0] ,im.shape[1] , 125), dtype=np.float64)
    sigmas = np.arange(k,k+0.125, 0.001)
    for i, sigma in enumerate(sigmas):
        log_hw = 3*np.ceil(np.max(sigmas))
        X, Y = np.meshgrid(np.arange(-log_hw, log_hw + 1, 1), np.arange(-log_hw, log_hw + 1, 1))
        log = 1/(2*np.pi*sigma**2)*(X**2/(sigma**2) + Y**2/(sigma**2) - 2)*np.exp(-(X**2 + Y**2)/(2*sigma**2))
        f_log = cv.filter2D(im_gray, cv.CV_64F, log)
        scale_space[:, :, i] = f_log

    indices = np.unravel_index(np.argmax(scale_space, axis=None), scale_space.shape)
    r = sigmas[indices[2]]*np.sqrt(2)

    #draw a circle around the detected blob
    cv.circle(im, (int(indices[1]), int(indices[0])), int(r), (0,255,0), 2)
fig, ax = plt.subplots()
plt.imshow(im)

