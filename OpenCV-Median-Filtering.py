#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:00:45 2024
@author: mac
"""

import cv2

image_path = "/Users/mac/Downloads/original.png"
image = cv2.imread(image_path)

median_filtered_image_cv2 = cv2.medianBlur(image, 5)
cv2_median_filtered_image_path = "cv2_median_filtered_image.png"
cv2.imwrite(cv2_median_filtered_image_path, median_filtered_image_cv2)
