# Copyright 2023 AE


import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import cv2 as cv


def lateralEffect(org_array):
    # Corresponding weights that we will add
    weights = np.zeros(org_array.shape)
    # The lateral effect that will be applied to each cube
    weaken_arr = org_array * .4
    row, column = weights.shape
    # Capturing the lateral effect in the weights array
    for i in range(row):
        for j in range(column):
            try:
                weights[i][j] = (weaken_arr[i][j-1] + 
                                 weaken_arr[i][j+1] +
                                 weaken_arr[i+1][j] + weaken_arr[i-1][j])
            except:
                continue
    # Returning the original image with the changed weights
    return org_array + weights



image = cv.imread('download5.jpg')
data_arr = np.array(image)

data_arr_bi = data_arr[:,:,:1].squeeze()

resized_image = cv.resize(data_arr_bi, (30,30))
print(resized_image.shape)
# plt.imshow(data_arr[:,:,:1]),plt.show()
ans = lateralEffect(resized_image)
plt.subplot(1, 2, 1, xlabel = "Input Image")
plt.imshow(resized_image)
plt.subplot(1, 2, 2, xlabel = "After lateral Effect")
plt.imshow(ans)
# plt.subplot(133), plt.imshow(ans - resized_image)
plt.show()






