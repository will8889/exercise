prices = {
    'banana':4,
    'apple':2,
    'orange':1.5,
    'pear':3
}

stocks = {
    'banana':5,
    'apple':5,
    'orange':5,
    'pear':5
}

for i in prices:
    print(i)
    print('price:',prices[i])
    print('stock:',stocks[i])

total = 0
for i in prices:
    total += prices[i] * stocks[i]

print("Total Earning:",total)
   