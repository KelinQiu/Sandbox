import random

MAX_INCREASE = 0.2  # 20%
MAX_DECREASE = 0.15  # 15%
MIN_PRICE = 0.1
MAX_PRICE = 10000.0
INITIAL_PRICE = 200.0
OUTPUT_FILE = "stock_output.txt"

# open output file for writing (this creates a new file if it doesn't exist)
out_file = open(OUTPUT_FILE, 'w')

price = INITIAL_PRICE
day = 0
print("Starting price: ${:,.2f}".format(price), file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    day += 1
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    # print("On day {} price is: ${:,.2f}".format(day, price))
    print("On day {} price is: ${:,.2f}".format(day, price), file=out_file)

# don't forget to close the file when we've finished with it
out_file.close()
