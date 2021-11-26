"""
CP1404
Shop calculator program to determine total (discounted) price
"""

total_price = 0
num_items = int(input("Number of items: "))
while num_items< 0:
    print("Invalid number of items!")
    num_items = int(input("Number of items: "))
for i in range(num_items):
    price_of_item= float(input("Price of item: "))
    total_price += price_of_item

if total_price > 100:

    total_price*= 0.9  # apply 10% discount

    print("Total price for ", num_items, " items is $", total_price, sep='')

# with string formatting for currency output
else:
    print("Total price for {} items is ${:.2f}".format(num_items, total_price))
