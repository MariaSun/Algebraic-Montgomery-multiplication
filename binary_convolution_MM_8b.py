#############################################
#08/18/2021 -- Maria Solyanik-Gorgone       #
#8bit binary convolution-based MM algorithm #
#############################################

import numpy as np

def high_low_bits(sequence, length_high, length_low):
	return sequence[:length_high], sequence[-length_low:]

def convert_in_number(sequence):
	number = 0
	for i in range(len(sequence)):
		number += 2**i * sequence[len(sequence)-i-1]

	return number

a_bar = np.array([1,1,1,0,0,1,1])
b_bar = np.array([1,1,1,1,1,0,0])

m = np.array([1,1,1,1,1,1,1,0,1])
M = np.array([1,0,1,0,1,0,1,1])
r = np.array([1,0,0,0,0,0,0,0,0,0])

a_b_bar = np.convolve(a_bar, b_bar)

overlap = 6#must be more than 5 for 16 digit multiplication

k1_high, k1_low = high_low_bits(a_b_bar, len(a_b_bar)-len(r)+1+overlap, len(r)-1)

k2 = np.convolve(k1_low, M)
high, k3 = high_low_bits(k2, len(r)-1, len(r)-1)

k4 = np.convolve(k3,m)
k4_high, k4_low = high_low_bits(k4, len(k4)-len(r)+1+overlap, len(r)-1)

move=int(len(k4_high) - len(k1_high))

k1_high = np.pad(k1_high, (move, 0), 'constant', constant_values=(0, 0))

one = np.zeros(len(k1_high))
one[len(m)-1] = 1

k5_high = k1_high + k4_high + one

res_bar = convert_in_number(k5_high/2**(overlap))

print(res_bar)

print((int(res_bar)*512) % 509)

