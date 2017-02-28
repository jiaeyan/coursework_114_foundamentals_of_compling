from fst import FST
import string, sys
from string import ascii_lowercase
from fsmutils import compose
'''
Jiajie Sven Yan
'''
def letters_to_numbers():
	"""
	Returns an FST that converts letters to numbers as specified by
	the soundex algorithm
	"""
	# Let's define our first FST
	f1 = FST('soundex-generate')

	# Indicate that '1' is the initial state
	f1.add_state('1')
	f1.initial_state = '1'
	for i in range(2,10):
		f1.add_state(str(i))
	for letter in string.letters:
		f1.add_arc('1','2',letter,letter)
	for letter in ['a','e','h','i','o','u','w','y']:
		for i in range(2,10):
			f1.add_arc(str(i),'3',letter,'')
	for letter in ['b','f','p','v']:
		for i in range(2,10):
			if str(i)=='4':f1.add_arc(str(i),'4',letter,'')
			else:f1.add_arc(str(i),'4',letter,'1')		
	for letter in ['c','g','j','k','q','s','x','z']:
		for i in range(2,10):
			if str(i)=='5':f1.add_arc(str(i),'5',letter,'')
			else:f1.add_arc(str(i),'5',letter,'2')
	for letter in ['d','t']:
		for i in range(2,10):
			if str(i)=='6':f1.add_arc(str(i),'6',letter,'')
			else:f1.add_arc(str(i),'6',letter,'3')
	for letter in ['l']:
		for i in range(2,10):
			if str(i)=='7':f1.add_arc(str(i),'7',letter,'')
			else:f1.add_arc(str(i),'7',letter,'4')	
	for letter in ['m','n']:
		for i in range(2,10):
			if str(i)=='8':f1.add_arc(str(i),'8',letter,'')
			else:f1.add_arc(str(i),'8',letter,'5')
	for letter in ['r']:
		for i in range(2,10):
			if str(i)=='9':f1.add_arc(str(i),'9',letter,'')
			else:f1.add_arc(str(i),'9',letter,'6')
		
	# Set all the final states
	for i in range(2,10):
		f1.set_final(str(i))

	return f1

def truncate_to_three_digits():
	"""
	Create an FST that will truncate a soundex string to three digits
	"""

	# Ok so now let's do the second FST, the one that will truncate
	# the number of digits to 3
	f2 = FST('soundex-truncate')

	# Indicate initial and final states
	f2.add_state('1')
	f2.initial_state = '1'
	for i in range(2,6):
		f2.add_state(str(i))
	for i in range(2,6):
		f2.set_final(str(i))
	
	for letter in string.letters:
		f2.add_arc('1','2',letter,letter)
		f2.add_arc('2','2',letter,letter)
	for letter in ['1','2','3','4','5','6']:
		f2.add_arc('1','3',letter,letter)
		f2.add_arc('2','3',letter,letter)
		f2.add_arc('3','4',letter,letter)
		f2.add_arc('4','5',letter,letter)
		f2.add_arc('5','5',letter,'')

	return f2

def add_zero_padding():
	# Now, the third fst - the zero-padding fst
	f3 = FST('soundex-padzero')
	
	f3.add_state('1')	
	f3.initial_state = '1'
	for i in range(2,8):
		f3.add_state(str(i))
	f3.set_final('5')
	f3.set_final('7')
	for letter in string.letters:
		f3.add_arc('1','2',letter,letter)
		f3.add_arc('2','2',letter,letter)
	for letter in ['1','2','3','4','5','6']:
		f3.add_arc('1','3',letter,letter)
		f3.add_arc('2','3',letter,letter)
		f3.add_arc('3','4',letter,letter)
		f3.add_arc('4','5',letter,letter)
		f3.add_arc('3','6','','0')
		f3.add_arc('6','7','','0')
		f3.add_arc('4','7','','0')

	return f3

def soundex_convert(name_string):
	"""Combine the three FSTs above and use it to convert a name into a Soundex"""
	char_list=[char for char in name_string]
	target=compose(char_list,letters_to_numbers(),truncate_to_three_digits(),add_zero_padding())
	return ''.join(target[0])

if __name__ == '__main__':
	user_input = input().strip()
	f1 = letters_to_numbers()
	f2 = truncate_to_three_digits()
	f3 = add_zero_padding()

		
	if user_input:
		print("%s -> %s" % (user_input, soundex_convert(tuple(user_input))))

