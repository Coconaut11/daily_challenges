# COMPLETED

prices = [9, 11, 8, 5, 7, 10]

def get_max_possible_benefit(prices):
	hi = 0
	for i in range(len(prices)):
		for j in range(i+1, len(prices)):
			profit = prices[j] - prices[i]
			if profit > hi:
				hi = profit
	return hi

print(get_max_possible_benefit(prices))
