from src.utilities import bits

PBOX = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 8, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]


def permute(data):
	data = bits.bytes2bits(data)
	new_data = ''
	for bit_idx in range (0, len(data), 32) :
		array_bit = data[bit_idx:bit_idx+32]
		for idx in range (0,len(array_bit)) :
			new_data = new_data + array_bit[PBOX[idx]-1]
	new_data = bits.bits2bytes(new_data)
	return(new_data)
