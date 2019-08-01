# Zenith is at an index, nadir is at an index
# Zenith at 0, nadir at where your original encoded value index was
# Encoding:
# Left Encode
# Start with the left cipher, which is the cipher we want to encode to
# Shift the entire alphabet so that your encoded letter is at your zenith
# The letter that is mapped by the nadir from right to left is the letter of interest
# Drop Zenith+1 and store that somewhere
# Shift Zenith+2:Nadir one to the left
# Insert the value from before into Nadir
# Assumption:  Loop invariant always holds zenith at character 0
def encode_left(left_encode_string, character_index):
	"""
	param: left_encode_string: the string that starts the loop invariant
	param: character_index: the character_index that will be the mapped key from encode right
	return: the encoded string
	"""
	nadir = character_index
	zenith = 0
	new_shift_string = [''] * len(left_encode_string)
	# Shift character index to 0
	for index, value in enumerate(left_encode_string):
			new_shift_string[index-character_index+1] = value

	# pop index 1
	new_index_char = new_shift_string[1]
	# shift to char 1 from 2 to character index
	for index in range(1, character_index):
		if index+1 == len(left_encode_string):
			new_shift_string[index] = new_shift_string[0]
		else:
			new_shift_string[index] = new_shift_string[index+1]
	new_shift_string[character_index] = new_index_char
	
	new_shift_string = ''.join(new_shift_string)

	return new_shift_string

# Right Encode
# Shift the entire alphabet so that your enciphered value is at the zenith (doesn't matter what direction)
# Shift the entire alphabet one more position to the left
# Extract the value at Zenith+2
# Shift all the letters starting from Zenith+3 to Nadir one left
# Insert the extracted letter at Nadir

'PTLNBQDEOYSFAVZKGJRIHWXUMC'
def encode_right(right_encode_string, character_index):
	
# Decoding:
# Left Decode
#

# Right Decode 

encode_left('HXUCZVAMDSLKPEFJRIGTWOBNYQ', 13)