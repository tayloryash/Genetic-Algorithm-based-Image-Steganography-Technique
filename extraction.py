import math
import numpy as np
from PIL import Image
import copy

def zero(x_offset, y_offset, stego):
    secret = [0]*128*64*8
    l = 0
    val = 0
    total = 128 * 256
    mx_col = 256
    mn_row = -1
    mx_row = 128
    while total != 0:
        val = stego[x_offset][y_offset]%4
        secret[l+1] = val%2
        val = val // 2
        secret[l] = val
        y_offset += 1
        if y_offset == mx_col:
            x_offset -= 1
            if x_offset == mn_row:
                x_offset = mx_row - 1
            y_offset = 0
        l += 2
        total -= 1
    return secret

def one(x_offset, y_offset, stego):
    val = 0
    secret = [0] * 128 * 64 * 8
    l = 0
    prev = 0
    total = 128 * 256
    mx_col = 256
    mn_col = -1
    mn_row = -1
    mx_row = 128
    while (total != 0):
        val = stego[x_offset][y_offset] % 4
        secret[l + 1] = val % 2
        val = val // 2
        secret[l] = val
        x_offset += 1
        if x_offset == mx_row:
            y_offset -= 1
            if y_offset == mn_col:
                y_offset = mx_col - 1
            x_offset = 0
        l += 2
        total -= 1
    return secret

def two(x_offset, y_offset, stego):
    secret = [0] * 128 * 64 * 8
    val = 0
    l = 0
    prev = 0
    mx_col = 256
    mn_col = -1
    mn_row = -1
    mx_row = 128
    total = 128 * 256
    while (total != 0):
        val = stego[x_offset][y_offset] % 4
        secret[l + 1] = val % 2
        val = val // 2
        secret[l] = val
        y_offset -= 1
        if y_offset == mn_col:
            x_offset += 1
            if x_offset == mx_row:
                x_offset = 0
            y_offset = mx_col - 1
        l += 2
        total -= 1
    return secret

def three(x_offset, y_offset, stego):
    secret = [0] * 128 * 64 * 8
    val = 0
    l = 0
    prev = 0
    mx_col = 256
    mn_col = -1
    mn_row = -1
    mx_row = 128
    total = 128 * 256
    while (total != 0):
        val = stego[x_offset][y_offset] % 4
        secret[l + 1] = val % 2
        val = val // 2
        secret[l] = val
        x_offset -= 1
        if x_offset == mn_col:
            y_offset += 1
            if y_offset == mx_col:
                y_offset = 0
            x_offset = mx_row - 1
        l += 2
        total -= 1
    return secret

def four(x_offset, y_offset, stego):
    secret = [0] * 128 * 64 * 8
    val = 0
    l = 0
    prev = 0
    mx_col = 256
    mn_col = -1
    mn_row = -1
    mx_row = 128
    total = 128 * 256
    while (total != 0):
        val = stego[x_offset][y_offset] % 4
        secret[l + 1] = val % 2
        val = val // 2
        secret[l] = val
        y_offset += 1
        if y_offset == mx_col:
            x_offset += 1
            if x_offset == mx_row:
                x_offset = 0
            y_offset = 0
        l += 2
        total -= 1
    return secret

def five(x_offset, y_offset, stego):
    secret = [0] * 128 * 64 * 8
    val = 0
    l = 0
    prev = 0
    mx_col = 256
    mn_col = -1
    mn_row = -1
    mx_row = 128
    total = 128 * 256
    while (total != 0):
        val = stego[x_offset][y_offset] % 4
        secret[l + 1] = val % 2
        val = val // 2
        secret[l] = val
        x_offset += 1
        if x_offset == mx_row:
            y_offset += 1
            if y_offset == mx_col:
                y_offset = 0
            x_offset = 0
        l += 2
        total -= 1
    return secret

def six(x_offset, y_offset, stego):
    secret = [0] * 128 * 64 * 8
    val = 0
    l = 0
    prev = 0
    mx_col = 256
    mn_col = -1
    mn_row = -1
    mx_row = 128
    total = 128 * 256
    while (total != 0):
        val = stego[x_offset][y_offset] % 4
        secret[l + 1] = val % 2
        val = val // 2
        secret[l] = val
        y_offset -= 1
        if y_offset == mn_col:
            x_offset -= 1
            if x_offset == mn_row:
                x_offset = mx_row - 1
            y_offset = mx_col - 1
        l += 2
        total -= 1
    return secret

def seven(x_offset, y_offset, stego):
    secret = [0] * 128 * 64 * 8
    val = 0
    l = 0
    prev = 0
    mx_col = 256
    mn_col = -1
    mn_row = -1
    mx_row = 128
    total = 128 * 256
    while (total != 0):
        val = stego[x_offset][y_offset] % 4
        secret[l+1] = val % 2
        val = val // 2
        secret[l] = val
        x_offset -= 1
        if x_offset == mn_row:
            y_offset -= 1
            if y_offset == mn_col:
                y_offset = mx_col - 1
            x_offset = mx_row - 1
        l += 2
        total -= 1
    return secret

def eight(x_offset, y_offset, stego):
    secret = [0] * 128 * 128 * 8
    val = 0
    l = 0
    prev = 0
    mx_col = 256
    mn_col = -1
    mn_row = -1
    mx_row = 128
    total = 128 * 256
    while (total != 0):
        val = stego[x_offset][y_offset] % 4
        secret[l + 1] = val % 2
        val = val // 2
        secret[l] = val
        if x_offset % 2 == 0:
            y_offset += 1
            if y_offset == mx_col:
                x_offset += 1
                y_offset = mx_col - 1
        else:
            y_offset -= 1
            if y_offset == mn_col:
                x_offset += 1
                if x_offset == mx_row:
                    x_offset = 0
                y_offset = 0
        l += 2
        total -= 1
    return secret

def nine(x_offset, y_offset, stego):
    secret = [0] * 128 * 64 * 8
    val = 0
    l = 0
    prev = 0
    mx_col = 256
    mn_col = -1
    mn_row = -1
    mx_row = 128
    total = 128 * 256
    while (total != 0):
        val = stego[x_offset][y_offset] % 4
        secret[l + 1] = val % 2
        val = val // 2
        secret[l] = val
        if y_offset % 2 == 0:
            x_offset += 1
            if x_offset == mx_row:
                y_offset -= 1
                if y_offset == mn_col:
                    y_offset = mx_col - 1
                x_offset = mx_row - 1
        else:
            x_offset -= 1
            if x_offset == mn_row:
                y_offset -= 1
                x_offset = 0
        l += 2
        total -= 1
    return secret

def ten(x_offset, y_offset, stego):
    secret = [0] * 128 * 64 * 8
    val = 0
    l = 0
    prev = 0
    mx_col = 256
    mn_col = -1
    mn_row = -1
    mx_row = 128
    total = 128 * 256
    while (total != 0):
        val = stego[x_offset][y_offset] % 4
        secret[l + 1] = val % 2
        val = val // 2
        secret[l] = val
        if x_offset % 2 == 0:
            y_offset -= 1
            if y_offset == mn_col:
                y_offset = 0
                x_offset -= 1
                if x_offset == mn_row:
                    x_offset = mx_row - 1
        else:
            y_offset += 1
            if y_offset == mx_col:
                y_offset = mx_col - 1
                x_offset -= 1
        l += 2
        total -= 1
    return secret

def eleven(x_offset, y_offset, stego):
    secret = [0] * 128 * 64 * 8
    val = 0
    l = 0
    prev = 0
    mx_col = 256
    mn_col = -1
    mn_row = -1
    mx_row = 128
    total = 128 * 256
    while (total != 0):
        val = stego[x_offset][y_offset] % 4
        secret[l + 1] = val % 2
        val = val // 2
        secret[l] = val
        if y_offset % 2 == 0:
            x_offset -= 1
            if x_offset == mn_row:
                x_offset = 0
                y_offset += 1
        else:
            x_offset += 1
            if x_offset == mx_row:
                x_offset = mx_row - 1
                y_offset += 1
                if y_offset == mx_col:
                    y_offset = 0
        l += 2
        total -= 1
    return secret

def twelve(x_offset, y_offset, stego):
    secret = [0] * 128 * 64 * 8
    val = 0
    l = 0
    prev = 0
    mx_col = 256
    mn_col = -1
    mn_row = -1
    mx_row = 128
    total = 128 * 256
    while (total != 0):
        val = stego[x_offset][y_offset] % 4
        secret[l + 1] = val % 2
        val = val // 2
        secret[l] = val
        if y_offset % 2 == 0:
            x_offset -= 1
            if x_offset == mn_row:
                x_offset = 0
                y_offset -= 1
                if y_offset == mn_col:
                    y_offset = mx_col - 1
        else:
            x_offset += 1
            if x_offset == mx_row:
                x_offset = mx_row - 1
                y_offset -= 1
        l += 2
        total -= 1
    return secret

def thirteen(x_offset, y_offset, stego):
    secret = [0] * 128 * 64 * 8
    val = 0
    l = 0
    prev = 0
    mx_col = 256
    mn_col = -1
    mn_row = -1
    mx_row = 128
    total = 128 * 256
    while (total != 0):
        val = stego[x_offset][y_offset] % 4
        secret[l + 1] = val % 2
        val = val // 2
        secret[l] = val
        if x_offset % 2 == 0:
            y_offset += 1
            if y_offset == mx_col:
                y_offset = mx_col - 1
                x_offset -= 1
                if x_offset == mn_row:
                    x_offset = mx_row - 1
        else:
            y_offset -= 1
            if y_offset == mn_col:
                y_offset = 0
                x_offset -= 1
        l += 2
        total -= 1
    return secret

def fourteen(x_offset, y_offset, stego):
    secret = [0] * 128 * 64 * 8
    val = 0
    l = 0
    prev = 0
    mx_col = 256
    mn_col = -1
    mn_row = -1
    mx_row = 128
    total = 128 * 256
    while (total != 0):
        val = stego[x_offset][y_offset] % 4
        secret[l + 1] = val % 2
        val = val // 2
        secret[l] = val
        if y_offset % 2 == 0:
            x_offset += 1
            if x_offset == mx_row:
                x_offset = mx_row-1
                y_offset += 1
        else:
            x_offset -= 1
            if x_offset == mn_row:
                x_offset =  0
                y_offset += 1
                if y_offset == mx_col:
                    y_offset = 0
        l += 2
        total -= 1
    return secret

def fifteen(x_offset, y_offset, stego):
    secret = [0] * 128 * 64 * 8
    val = 0
    l = 0
    prev = 0
    mx_col = 256
    mn_col = -1
    mn_row = -1
    mx_row = 128
    total = 128 * 256
    while (total != 0):
        val = stego[x_offset][y_offset] % 4
        secret[l + 1] = val % 2
        val = val // 2
        secret[l] = val
        if x_offset % 2 == 0:
            y_offset -= 1
            if y_offset == mn_col:
                y_offset = 0
                x_offset += 1
        else:
            y_offset += 1
            if y_offset == mx_col:
                y_offset = mx_col - 1
                x_offset += 1
                if x_offset == mx_row:
                    x_offset = 0
        l += 2
        total -= 1
    return secret

switcher = {
        0: zero,
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,
        11: eleven,
        12: twelve,
        13: thirteen,
        14: fourteen,
        15: fifteen
    }

def raster_order(dir_input, x_offset, y_offset, stego):
    func = switcher[dir_input](x_offset, y_offset, stego)
    return func

def getValue(arr) :
    res = int("".join(str(x) for x in arr), 2)
    return res

def return_secret(stego, population):
    temp_stego = copy.deepcopy(stego)
    x_offset = getValue(population[14:21])
    y_offset = getValue(population[6:14])
    direction = getValue(population[2:6])
    sb_pole = getValue(population[1:2])
    sb_dir = getValue(population[0:1])

    secret = raster_order(direction, x_offset, y_offset, temp_stego)

    if (sb_pole):
        for i in range(len(secret)):
            if secret[i] == 0:
                secret[i] = 1
            else:
                secret[i] = 0

    if (sb_dir):
        secret.reverse()
    # print(np.array(secret))
    return secret
