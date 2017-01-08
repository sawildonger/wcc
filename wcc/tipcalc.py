cost=raw_input('How much was your meal?')
tip = 0.20 * float(cost)
print('You should tip $'+str(tip))
print('Your total cost would be $'+str(float(cost)+float(tip)))