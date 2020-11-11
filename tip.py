# tip.py - starter code
# this program is used to calculate tips when ordering pizza or getting a cab

def calculate_tip(amount, percentage):
	if not isinstance(amount, int):
		raise TypeError('Please provide an integer argument')
	if amount<0:
		raise ValueError('Please provide a positive integer')
	return amount * percentage / 100

def tip_for_pizza(amount):
	return calculate_tip(amount, 4)

def tip_for_ride(amount):
	return calculate_tip(amount, 10)

def print_message(item, amount, tip):
	print('Tip calculated for {} for {:.2f} is {:.2f}\n'.format(item, amount, tip))

# Some manual tests for the functions above


