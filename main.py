import cv2
from copy import copy, deepcopy
import helper as h
import direction_gene as d
import extraction as e
import numpy as np
from PIL import Image
import random
import math

# random.seed(1)

# import sys
# sys.setrecursionlimit(1000)


# getting host image
img = cv2.imread("hostim.jpg", 0)

# getting secret image
sec_img = cv2.imread("secret2.png", 0)
y_ = deepcopy(img)
x_ = deepcopy(sec_img)
# print(x_)

# converting to pixels
host = y_.tolist()
pix_secret = x_.tolist()

# print(pix_secret)

# split host in 2 parts
first_host, second_host = h.split_matrix(host, 128, 256)
first_secret, second_secret = h.split_matrix(pix_secret, 64, 128)

# if first_secret[0][127] == pix_secret[0][127]:
#     print(first_secret)

#  converting decimal to binary
for i in range(64):
    for j in range(128):
        first_secret[i][j] = bin(first_secret[i][j]).replace("0b", "")

for i in range(64):
    for j in range(128):
        second_secret[i][j] = bin(second_secret[i][j]).replace("0b", "")

# print(first_secret[0][0])

# if(first_host[127][255] == host[127][255]):
#     print(len(first_host))
# if(second_host[127][255] == host[255][255]):
#     print(len(second_host))

# converting to 8-bit pixels
secret_1 = []
secret_1 += h.conversion_8bit(first_secret, 64, 128)

secret_2 = []
secret_2 += h.conversion_8bit(second_secret, 64, 128)
# print(secret_1[0:8])
# print(len(secret))
# print(second_secret[0][127], secret_2[1016:1024])

# getting the psnr of stego image
# psnr, stego = d.return_psnr(host,secret)


# initialize population
best = -100000
best_stego1 = []
best_stego2 = {}
populations = [[random.random() for x in range(21)] for i in range(300)]
# print((populations))
parents = []
best_population = []


# print(populations)


# fitness score calculation ............
def fitness_score(xhost, xsecret, type):
    global populations, best, best_stego1, best_stego2, best_population
    fit_value = []
    fit_score = []
    all_stego = []
    for i in range(300):
        f, stego = d.return_psnr(xhost, xsecret, populations[i], type)
        fit_value.append(f)
        all_stego.append(list(stego))
        best_stego2[f] = stego
    # print(fit_value)
    if(type == 1):
        fit_value, populations, all_stego = zip(*sorted(zip(fit_value, populations, all_stego), reverse=True))
    else:
        fit_value, populations, all_stego = zip(*sorted(zip(fit_value, populations, all_stego)))
    best = fit_value[0]
    populations = list(populations)
    best_population = populations[0]
    best_stego1 = all_stego[0]


# fitness_score()
# print(len(all_stego), type(best_stego1))

# Tournament Selection
def tournament(population, xhost, xsecret, type):
    candidate1 = population[random.randint(0, 299)]
    candidate2 = population[random.randint(0, 299)]
    while candidate1 == candidate2:
        candidate2 = population[random.randint(0, 299)]

    f1, s1 = d.return_psnr(xhost, xsecret, candidate1, type)
    f2, s2 = d.return_psnr(xhost, xsecret, candidate2, type)
    if(type == 2):
        if(f1>f2): return  candidate2
        return candidate1
    if f1 > f2:
        return candidate1
    return candidate2


def selectparent(xhost, xsecret, type):
    global parents
    parents = []
    # global populations , parents
    for _ in range(150):
        child = tournament(populations, xhost, xsecret, type)
        parents.append(child)
    # parents = populations[0:150]
    # print(len(parents))


# selectparent()
#
# #
def crossover():
    global parents

    cross_point = random.randint(0, 20)
    offsprings = []
    p_crossover = 0.7
    for j in range(75):
        if random.random() > p_crossover:
            offspring1 = parents[2 * j]
            offspring2 = parents[2 * j + 1]
        else:
            offspring1 = parents[2 * j][0:cross_point + 1] + parents[2 * j + 1][cross_point + 1:21]
            # for i in range (6):
            #     offspring1[i+16] = random.randint(0, 1)
            # print(type(offspring1))
            # parents = parents + tuple([offspring1])

            offspring2 = parents[2 * j + 1][0:cross_point + 1] + parents[2 * j][cross_point + 1:21]
            # for i in range(6):
            #     offspring2[i + 16] = random.randint(0, 1)
        offsprings.append(offspring1)
        offsprings.append(offspring2)

    parents = parents + offsprings
    # print(len(parents), len(offsprings))


# crossover()
#
def mutation():
    mutation_rate = 0.04
    global populations, parents

    if random.random() < mutation_rate:
        x = random.randint(0, 299)
        y = random.randint(0, 20)
        parents[x][y] = 1 - parents[x][y]
    populations = parents
    # print(len(populations))


# mutation()
#
# # [1,0,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,0,0,0,1,0]
#
for i in range(1):
    fitness_score(first_host, secret_1, 1)
    selectparent(first_host, secret_1, 1)
    crossover()
    mutation()
print("best score :")
print(best)
print("sequence........")
print(best_population)
# print("stego.........")
# print(best_stego1)
print(".....................")

best_first_half_stego = deepcopy(best_stego1)
best_first_half_psnr = best
best_first_population = deepcopy(best_population)

# def generate_population(threshold):
#     temp = [random.randint(0,1) for x in range(21)]
#     p1, s = d.return_psnr(second_host, secret, temp)
#     if threshold > p1:
#         return  generate_population(threshold)
#     return temp
#
# for i in range(300):
#    populations[i] = generate_population(best)
best_stego1 = []
best_stego2 = {}
populations = [[random.randint(0, 1) for x in range(21)] for i in range(300)]
# print((populations))
parents = []
best_population = []

for i in range(1):
    fitness_score(second_host, secret_2, 2)
    selectparent(second_host, secret_2, 2)
    crossover()
    mutation()

best_second_half_stego = best_stego1
best_second_half_distortion = best
best_second_population = best_population

print(best_first_half_psnr, best_second_half_distortion)

real_stego = [[0] * 256 for _ in range(256)]

for i in range(256):
    for j in range(256):
        if i < 128:
            real_stego[i][j] = best_first_half_stego[i][j]
        else:
            real_stego[i][j] = best_second_half_stego[i - 128][j]

best_psnr = h.get_psnr(real_stego, host)

print("psnr ", best_psnr)
# print(np.array(best_stego2[best]))

# if best_stego2[best] != best_stego1:
#     print(type(best_stego2[best]), type(best_stego1))

# # Extraction
print(np.array(best_first_half_stego))
new_secret_1 = e.return_secret(best_first_half_stego, best_first_population)#[:65536]
new_secret_2 = e.return_secret(best_second_half_stego, best_second_population)#[65536:]

print(np.array(new_secret_1).shape, np.array(new_secret_2).shape)
# print(np.array(new_secret_1))
# if h.getValue(new_secret[0:8]) == h.getValue(new_secret[8*128: 8*128+8]):
#     print("YES")

# print(h.getValue(new_secret[0:8]), h.getValue(new_secret[8*128: 8*128+8]))
real_secret_1 = np.array(h.convert_decimal(new_secret_1, 64, 128))

real_secret_2 = np.array(h.convert_decimal(new_secret_2, 64, 128))
real_secret = [[0] * 128 for _ in range(128)]

print(real_secret_1[0][0], real_secret_2[0][0])

for i in range(128):
    for j in range(128):
        if i < 64:
            real_secret[i][j] = real_secret_1[i][j]
        else:
            real_secret[i][j] = real_secret_2[i - 64][j]

# print(x_)
# print(real_secret)
print(np.array_equal(x_, real_secret))
array = np.array(real_secret, dtype=np.uint8)
new_image = Image.fromarray(array)
new_image.save("extracted_secret.png")


#
# # importing library for plotting
# from matplotlib import pyplot as plt
#
# # # reads an input image
# img = cv2.imread('stego.png', 0)
#
# # find frequency of pixels in range 0-255

# histr = cv2.calcHist([y_], [0], None, [256], [0, 256])
# #
# # # show the plotting graph of an image
# plt.plot(histr)
# plt.show()
# real_stego = np.array(real_stego, dtype=np.uint8)
# histr = cv2.calcHist([real_stego], [0], None, [256], [0, 256])
# #
# # # show the plotting graph of an image
# plt.plot(histr)
# plt.show()
#
# histr = cv2.calcHist(y_, [0], None, [256], [0, 256])
# #
# # # show the plotting graph of an image
# plt.plot(histr)
# plt.show()
#
# histr = cv2.calcHist(real_stego, [0], None, [256], [0, 256])
# #
# # # show the plotting graph of an image
# plt.plot(histr)
# plt.show()
