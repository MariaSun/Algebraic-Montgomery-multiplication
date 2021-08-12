##########################################################
#08/12/2021 -- Maria Solyanik-Gorgone                    #
#Exact algebraic algorithm for Montgomery multiplication.#
##########################################################

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import cmath 
import math
import cv2

def check_if_prime(num):
	if num > 1:
	    for i in range(2, int(num/2)+1):
	        if (num % i) == 0:
	            print(num, "is not a prime number, must be a prime!")
	            break

def hcfnaive(a,b):
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)

def find_inverse(a, mod):
	for i in range(1,10000000):
		if (i*a) % mod == 1: 
			res = i
			break
	return res

def bar_calculation(num, res, mod):
	return (num * res) % mod


a = 28510
b = 38672

m = 36057
r = 2**(17)

if hcfnaive(m,r)!=1: print('gcd(m, r)==1 and it is not, pick m as relative prime of r!')

R = find_inverse(r, m)
M = find_inverse(-m, r)

if (r*R) - (m*M)!=1: print('The inverse of m and r produced errors. Check!')

a_bar = bar_calculation(a, r, m)
b_bar = bar_calculation(b, r, m)

second = ((a_bar*b_bar*M) % r) * m

c_bar = ((a_bar*b_bar) + second)/r

c = bar_calculation(c_bar, R, m)

if c % 1 != 0: print('Result must be integer! Check the algorithm!')

print(int(c))








