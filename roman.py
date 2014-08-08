ONE = "I"
FIVE = "V"
TEN = "X"
FIFTY = "L"
HUNDRED = "C"
FIVE_HUNDRED = "D"
THOUSAND = "M"

def int_to_roman(num):
	list_nums = [int(x) for x in str(num)]
	print list_nums
	mult = 1
	new_nums = []
	for item in list_nums[::-1]:
		new_nums.append(item * mult)
		mult = mult * 10
	final = ""
	for x in new_nums[::-1]:
		print x
		final = final + (digit_to_roman(x))
	return final
		
def digit_to_roman(digit):
	length = len(str(digit))
	print length
	if length == 1:
		one = ONE
		five = FIVE
		ten = TEN
	elif length == 2:
		one = TEN
		five = FIFTY
		ten = HUNDRED
	elif length == 3:
	    one = HUNDRED
	    five = FIVE_HUNDRED
	    ten = THOUSAND
	elif length == 4:
		one = THOUSAND
		five = "$"
		ten = "%"
	else:
		return ""
	first = int(str(digit)[0])
	if (1 <= first) and (first <= 3):
		return first * one
	elif first == 4:
		return one + five
	elif first == 5:
		return five
	elif (6 <= first) and (first <= 8):
		return five + ((first-5)*one)
	else:
		return (10-first)*one + ten
	
	    
		
	
	new_nums = new_nums[::-1]
	print new_nums
		
	
ans = int_to_roman(5999)
print ans
