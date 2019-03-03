import copy 

def shift_rows(data):
	table = []
	for row_idx in range (0,4) :
		row = []
		for column_idx in range (0,len(data)//4) :
			row.append(data[row_idx*(len(data)//4) + column_idx])
		table.append(row)

	new_table = copy.deepcopy(table)
	for row_idx in range (0, 4) :
		for column_idx in range (0,len(data)//4) :
			new_table[row_idx][(column_idx+row_idx)%(len(data)//4)] = table[row_idx][column_idx]
	new_table = ''.join([''.join(x) for x in new_table]) 
	return(new_table)