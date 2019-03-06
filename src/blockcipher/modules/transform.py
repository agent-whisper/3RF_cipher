import copy 
from src.utilities import bytes as byte
import numpy as np

def shift_rows(data):
	table = []
	if (len(data) == 4) :
		len_row = 2
	if (len(data) > 4) :
		len_row = 4
		
	for row_idx in range (0,len_row) :
		row = []
		for column_idx in range (0,len(data)//len_row) :
			row.append(data[row_idx*(len(data)//len_row) + column_idx])
		table.append(row)
	new_table = copy.deepcopy(table)
	for row_idx in range (0, len_row) :
		for column_idx in range (0,len(data)//len_row) :
			new_table[row_idx][(column_idx+row_idx)%(len(data)//len_row)] = table[row_idx][column_idx]

	new_table = bytes(np.array(new_table).flatten().tolist())
	return(new_table)