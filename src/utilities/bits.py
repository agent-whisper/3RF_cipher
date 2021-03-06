from src.utilities import bits

def bits2bytes(bits):
	return(bytes([int(''.join(x), 2) for x in zip(*[iter(bits)]*8)]))

def bytes2bits(bytes) :
	return(''.join('{0:08b}'.format(x) for x in bytes))