def multiply (a,b):
	result = a*b
	return result

solution = multiply (4,5)
print(solution)

def cube(a):
	product = a*a*a
	return product

print(cube(3))

def isPositive(a):
    return a > 0
	
print(isPositive(4))


def mystery(x, y, z):
	solution = x + (y*z)
	return solution



# Test this function:
print mystery('Hello', 3, '!') # Expected: 'Hello!!!'
print mystery('Goodbye', 2, '@') # Expected: 'Goodbye@@'


def calculate_tip(meal_price,rating):

	if rating == 'A':
		tip = .2*meal_price
	elif rating == 'B':
		tip = .18*meal_price
	else:
		tip = .15*meal_price
	return tip
	
print(calculate_tip(30.50, 'C')) # Expected: 4.575
print(calculate_tip(15.00, 'B')) # Expected: 2.7
print(calculate_tip(20.00, 'A')) # Expected: 4	