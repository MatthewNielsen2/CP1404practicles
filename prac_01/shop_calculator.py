number_of_items = int(input("Number of items: "))
total = 0
while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total = total + price_of_item
if total >= 100:
    total = total - (total * 0.10)
print(total)
