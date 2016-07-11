# Change Maker - Calculate Change for a Dollar Store
# Bill Power
# 7/3/16

price = input('Enter Cost of Item:\n')
paid  = input('Enter Amount Paid:\n')

change = paid - price

print('Change to make:')
print(change)

q = change / 25
change = change - q*25

d = change / 10
change = change - d*10

n = change / 5
change = change - n*5

p = change

print("Q: {} \nD: {}\nN: {}\nP: {}").format( q, d, n, p )