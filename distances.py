# from skimage import io
# import matplotlib.pyplot as plt
# image = io.imread('stego.png')
# ax = plt.hist(image.ravel(), bins = 256)
# plt.show()
from copy import copy,deepcopy
from PIL import Image
import cv2
img  = cv2.imread('distortion_stego.jpg', 0)
s= deepcopy(img)
stego = s.tolist()

stego_bin = [0 for _ in range(256)]

for i in range(256):
    for j in range(256):
        stego_bin[stego[i][j]] += 1

img = cv2.imread('hostim.jpg', 0)
h = deepcopy(img)
host = h.tolist()

host_bin = [0 for _ in range(256)]
for i in range(256):
    for j in range(256):
        host_bin[host[i][j]] += 1
#
p = 256*256
# for i in range(256): p1 += host_bin[i]
#
# p2 = 0
# for i in range(256): p2 += host_bin[i]


#
P = [0 for _ in range(256)]
Q = [0 for _ in range(256)]
#
for i in range(256):
    P[i] = stego_bin[i]/p
    Q[i] = host_bin[i]/p

import math
d = 0
for i in range(256):
    # if(Q[i] >0and P[i]>0):
        d += math.sqrt(P[i]*Q[i])
print("Bhattacharya ", -math.log(d))

d = 0
for i in range(256):
    if(P[i]+Q[i]):
        d += ((P[i]-Q[i])**2)/(P[i]+Q[i])

# d = -math.log(d)

print("Chisquare ", (d))

# d = 0
# for i in range(256):
#     # if(Q[i] >0and P[i]>0):
#         d += ((P[i]-Q[i])**2)
# print(math.sqrt(d))

d = 0
for i in range(256):
    if(Q[i] >0and P[i]>0):
        d += (P[i]-Q[i])*(math.log(P[i]/Q[i]))
print("Jeffrey " ,(d))


d = 0
for i in range(256):
    if (Q[i] > 0 and P[i] > 0):
        d += (P[i]) * (math.log(P[i] / Q[i]))
print("Kullback ", (d))

d = 0
for i in range(256):
    # if(Q[i] >0and P[i]>0):
        d  = max(d,  abs(P[i]-Q[i]))
print("KSD ", (d))

d = 0
for i in range(256):
    d += abs(P[i]-Q[i])
print("CB  ", (d))


d = 0
for i in range(256):
    d += ((P[i]-Q[i])**2)
print("Euclidean  ", math.sqrt(d))
