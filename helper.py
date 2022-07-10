
import math
import numpy as np
from PIL import Image
import copy


def conversion_8bit(pix, r, c):
    temp = []
    for i in range(r):
        for j in range(c):
            while (len(str((pix[i][j]))) != 8):
                pix[i][j] = "0" + str(pix[i][j])
            temp += pix[i][j]
    # print(len(temp))
    return temp

def getValue(arr) :
    res = int("".join(str(x) for x in arr), 2)
    return res


def convert_decimal(arr, r, c):
    temp = [[0]*c for _ in range(r)]
    k = 0
    for i in range(r):
        for j in range(c):
            temp[i][j] = getValue(arr[k:k+8])
            k += 8
            # print(temp[i][j])
    # print(temp)
    # array = np.array(temp, dtype=np.uint8)
    # new_image = Image.fromarray(array)
    # new_image.save("rs.png")
    return  temp

def split_matrix(mat, r, c):
    temp1 = [[0]*c for _ in range(r)]
    temp2 = [[0]*c for _ in range(r)]
    # print(type(temp1[1]), type(mat[1]))

    for i in range(c):
        for j in range (c):
            if(i<r):temp1[i][j] = mat[i][j]
            else: temp2[i-r][j] = mat[i][j]

    return  temp1, temp2

def get_psnr(stego, host):
    mse = 0;
    for i in range(256):
        for j in range(256):
            mse += (stego[i][j]-host[i][j]) * (stego[i][j]-host[i][j])
    mse = mse/(256*256)
    psnr = 10 * math.log10((255*255)/mse)
    return  psnr
