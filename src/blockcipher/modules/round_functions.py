from src.blockcipher.modules import pbox, sbox, transform
from src.utilities import bytes as byte

def rf_a(left_block, right_block, round_key_a):
	new_r = byte.xor_byte(right_block, round_key_a)
	new_r = transform.shift_rows(new_r)
	new_r = sbox.substitute(new_r)
	new_r = pbox.permute(new_r)
	new_l = byte.xor_byte(left_block, new_r)
	return(new_l)

def rf_b(left_block, right_block, round_key_b):
	new_r = byte.xor_byte(right_block, round_key_b)
	new_r = sbox.substitute(new_r)
	new_r = pbox.permute(new_r)
	new_l = byte.xor_byte(new_r, left_block)
	return(new_l)

def rf_c(left_block, right_block, round_key_c):
	new_r = byte.xor_byte(right_block, round_key_c)
	new_r = transform.shift_rows(new_r)
	new_r = pbox.permute(new_r)
	new_l = byte.xor_byte(new_r, left_block)
	return(new_l)


def rf_combination(block, round_key, combination_num):
	left_block = block[:len(block)//2]
	right_block = block[len(block)//2:]
	round_key_1 = round_key[:len(round_key)//2] 
	round_key_2 = round_key[len(round_key)//2:len(round_key)//2+len(round_key)//4]
	round_key_3 = round_key[len(round_key)//2+len(round_key)//4:]
	if (combination_num == 0) :
		left_block = rf_a(left_block, right_block, round_key_1)
		# left side
		new_left_block = left_block[:len(left_block)//2]
		new_right_block = left_block[len(left_block)//2:]

		second_block =  rf_b(new_left_block, new_right_block, round_key_2)
		fourth_block = new_right_block

		# right side
		new_left_block = right_block[:len(right_block)//2]
		new_right_block = right_block[len(right_block)//2:]

		first_block =  rf_c(new_left_block, new_right_block, round_key_3)
		third_block = new_right_block

	if (combination_num == 1) :
		left_block = rf_a(left_block, right_block, round_key_1)
		# left side
		new_left_block = left_block[:len(left_block)//2]
		new_right_block = left_block[len(left_block)//2:]

		second_block =  rf_c(new_left_block, new_right_block, round_key_2)
		fourth_block = new_right_block

		# right side
		new_left_block = right_block[:len(right_block)//2]
		new_right_block = right_block[len(right_block)//2:]

		first_block =  rf_b(new_left_block, new_right_block, round_key_3)
		third_block = new_right_block

	if (combination_num == 2) :
		left_block = rf_b(left_block, right_block, round_key_1)
		# left side
		new_left_block = left_block[:len(left_block)//2]
		new_right_block = left_block[len(left_block)//2:]

		second_block =  rf_a(new_left_block, new_right_block, round_key_2)
		fourth_block = new_right_block

		# right side
		new_left_block = right_block[:len(right_block)//2]
		new_right_block = right_block[len(right_block)//2:]

		first_block =  rf_c(new_left_block, new_right_block, round_key_3)
		third_block = new_right_block

	if (combination_num == 3) :
		left_block = rf_b(left_block, right_block, round_key_1)
		# left side
		new_left_block = left_block[:len(left_block)//2]
		new_right_block = left_block[len(left_block)//2:]

		second_block =  rf_c(new_left_block, new_right_block, round_key_2)
		fourth_block = new_right_block

		# right side
		new_left_block = right_block[:len(right_block)//2]
		new_right_block = right_block[len(right_block)//2:]

		first_block =  rf_a(new_left_block, new_right_block, round_key_3)
		third_block = new_right_block

	if (combination_num == 4) :
		left_block = rf_c(left_block, right_block, round_key_1)
		# left side
		new_left_block = left_block[:len(left_block)//2]
		new_right_block = left_block[len(left_block)//2:]

		second_block =  rf_a(new_left_block, new_right_block, round_key_2)
		fourth_block = new_right_block

		# right side
		new_left_block = right_block[:len(right_block)//2]
		new_right_block = right_block[len(right_block)//2:]

		first_block =  rf_b(new_left_block, new_right_block, round_key_3)
		third_block = new_right_block

	if (combination_num == 5) :
		left_block = rf_c(left_block, right_block, round_key_1)
		# left side
		new_left_block = left_block[:len(left_block)//2]
		new_right_block = left_block[len(left_block)//2:]
		second_block =  rf_b(new_left_block, new_right_block, round_key_2)
		fourth_block = new_right_block
		# right side
		new_left_block = right_block[:len(right_block)//2]
		new_right_block = right_block[len(right_block)//2:]

		first_block =  rf_a(new_left_block, new_right_block, round_key_3)
		third_block = new_right_block

	block = byte.merge_bytes([first_block,second_block,third_block,fourth_block])
	return(block)

def rf_inv_combination(block, round_key, combination_num):
	left_block = byte.merge_bytes([block[len(block)//4:len(block)//2], block[(len(block)*3)//4:]])
	right_block = byte.merge_bytes([block[:len(block)//4], block[len(block)//2:(len(block)*3)//4]])
	round_key_1 = round_key[:len(round_key)//2] 
	round_key_2 = round_key[len(round_key)//2:len(round_key)//2+len(round_key)//4]
	round_key_3 = round_key[len(round_key)//2+len(round_key)//4:]
	if (combination_num == 0) :
		# left side
		new_left_block = left_block[:len(left_block)//2]
		new_right_block = left_block[len(left_block)//2:]
		second_block =  rf_b(new_left_block, new_right_block, round_key_2)
		fourth_block = new_right_block
		left_block = byte.merge_bytes([second_block, fourth_block])

		# right side
		new_left_block = right_block[:len(right_block)//2]
		new_right_block = right_block[len(right_block)//2:]

		first_block =  rf_c(new_left_block, new_right_block, round_key_3)
		third_block = new_right_block
		right_block = byte.merge_bytes([first_block, third_block])
		left_block = rf_a(left_block, right_block, round_key_1)

	if (combination_num == 1) :
		# left side
		new_left_block = left_block[:len(left_block)//2]
		new_right_block = left_block[len(left_block)//2:]
		second_block =  rf_c(new_left_block, new_right_block, round_key_2)
		fourth_block = new_right_block
		left_block = byte.merge_bytes([second_block, fourth_block])

		# right side
		new_left_block = right_block[:len(right_block)//2]
		new_right_block = right_block[len(right_block)//2:]

		first_block =  rf_b(new_left_block, new_right_block, round_key_3)
		third_block = new_right_block
		right_block = byte.merge_bytes([first_block, third_block])
		left_block = rf_a(left_block, right_block, round_key_1)

	if (combination_num == 2) :
		# left side
		new_left_block = left_block[:len(left_block)//2]
		new_right_block = left_block[len(left_block)//2:]
		second_block =  rf_a(new_left_block, new_right_block, round_key_2)
		fourth_block = new_right_block
		left_block = byte.merge_bytes([second_block, fourth_block])

		# right side
		new_left_block = right_block[:len(right_block)//2]
		new_right_block = right_block[len(right_block)//2:]

		first_block =  rf_c(new_left_block, new_right_block, round_key_3)
		third_block = new_right_block
		right_block = byte.merge_bytes([first_block, third_block])
		left_block = rf_b(left_block, right_block, round_key_1)

	if (combination_num == 3) :
		# left side
		new_left_block = left_block[:len(left_block)//2]
		new_right_block = left_block[len(left_block)//2:]
		second_block =  rf_c(new_left_block, new_right_block, round_key_2)
		fourth_block = new_right_block
		left_block = byte.merge_bytes([second_block, fourth_block])

		# right side
		new_left_block = right_block[:len(right_block)//2]
		new_right_block = right_block[len(right_block)//2:]

		first_block =  rf_a(new_left_block, new_right_block, round_key_3)
		third_block = new_right_block
		right_block = byte.merge_bytes([first_block, third_block])
		left_block = rf_b(left_block, right_block, round_key_1)

	if (combination_num == 4) :
		# left side
		new_left_block = left_block[:len(left_block)//2]
		new_right_block = left_block[len(left_block)//2:]
		second_block =  rf_a(new_left_block, new_right_block, round_key_2)
		fourth_block = new_right_block
		left_block = byte.merge_bytes([second_block, fourth_block])

		# right side
		new_left_block = right_block[:len(right_block)//2]
		new_right_block = right_block[len(right_block)//2:]

		first_block =  rf_b(new_left_block, new_right_block, round_key_3)
		third_block = new_right_block
		right_block = byte.merge_bytes([first_block, third_block])
		left_block = rf_c(left_block, right_block, round_key_1)

	if (combination_num == 5) :
		# left side
		new_left_block = left_block[:len(left_block)//2]
		new_right_block = left_block[len(left_block)//2:]
		second_block =  rf_b(new_left_block, new_right_block, round_key_2)
		fourth_block = new_right_block
		left_block = byte.merge_bytes([second_block, fourth_block])

		# right side
		new_left_block = right_block[:len(right_block)//2]
		new_right_block = right_block[len(right_block)//2:]

		first_block =  rf_a(new_left_block, new_right_block, round_key_3)
		third_block = new_right_block
		right_block = byte.merge_bytes([first_block, third_block])
		left_block = rf_c(left_block, right_block, round_key_1)


	# if (combination_num == 1) :
	# 	left_block = rf_a(left_block, right_block, round_key_1)
	# 	# left side
	# 	new_left_block = left_block[:len(left_block)//2]
	# 	new_right_block = left_block[len(left_block)//2:]

	# 	second_block =  rf_c(new_left_block, new_right_block, round_key_2)
	# 	fourth_block = new_right_block

	# 	# right side
	# 	new_left_block = right_block[:len(right_block)//2]
	# 	new_right_block = right_block[len(right_block)//2:]

	# 	first_block =  rf_b(new_left_block, new_right_block, round_key_3)
	# 	third_block = new_right_block

	# if (combination_num == 2) :
	# 	left_block = rf_b(left_block, right_block, round_key_1)
	# 	# left side
	# 	new_left_block = left_block[:len(left_block)//2]
	# 	new_right_block = left_block[len(left_block)//2:]

	# 	second_block =  rf_a(new_left_block, new_right_block, round_key_2)
	# 	fourth_block = new_right_block

	# 	# right side
	# 	new_left_block = right_block[:len(right_block)//2]
	# 	new_right_block = right_block[len(right_block)//2:]

	# 	first_block =  rf_c(new_left_block, new_right_block, round_key_3)
	# 	third_block = new_right_block

	# if (combination_num == 3) :
	# 	left_block = rf_b(left_block, right_block, round_key_1)
	# 	# left side
	# 	new_left_block = left_block[:len(left_block)//2]
	# 	new_right_block = left_block[len(left_block)//2:]

	# 	second_block =  rf_c(new_left_block, new_right_block, round_key_2)
	# 	fourth_block = new_right_block

	# 	# right side
	# 	new_left_block = right_block[:len(right_block)//2]
	# 	new_right_block = right_block[len(right_block)//2:]

	# 	first_block =  rf_a(new_left_block, new_right_block, round_key_3)
	# 	third_block = new_right_block

	# if (combination_num == 4) :
	# 	left_block = rf_c(left_block, right_block, round_key_1)
	# 	# left side
	# 	new_left_block = left_block[:len(left_block)//2]
	# 	new_right_block = left_block[len(left_block)//2:]

	# 	second_block =  rf_a(new_left_block, new_right_block, round_key_2)
	# 	fourth_block = new_right_block

	# 	# right side
	# 	new_left_block = right_block[:len(right_block)//2]
	# 	new_right_block = right_block[len(right_block)//2:]

	# 	first_block =  rf_b(new_left_block, new_right_block, round_key_3)
	# 	third_block = new_right_block

	# if (combination_num == 5) :
	# 	left_block = rf_c(left_block, right_block, round_key_1)
	# 	# left side
	# 	new_left_block = left_block[:len(left_block)//2]
	# 	new_right_block = left_block[len(left_block)//2:]
	# 	second_block =  rf_b(new_left_block, new_right_block, round_key_2)
	# 	fourth_block = new_right_block
	# 	# right side
	# 	new_left_block = right_block[:len(right_block)//2]
	# 	new_right_block = right_block[len(right_block)//2:]

	# 	first_block =  rf_a(new_left_block, new_right_block, round_key_3)
	# 	third_block = new_right_block

	block = byte.merge_bytes([left_block, right_block])
	return(block)


