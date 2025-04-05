# Input Data
items = ['Shirt', 'Pants', 'Shoes', 'Hat']
prices = [20.00, 30.00, 50.00, 10.00]
colors = ['Red', 'Blue', None, 'Black']
discounts = [10, 0, 20, 5]

# Ensure all lists have the same length
if not (len(items) == len(prices) == len(colors) == len(discounts)):
    raise ValueError("All input lists must have the same length.")

# Combine the lists into a list of tuples using zip
products = list(zip(items, prices, colors, discounts, strict=True))

# Calculate the discounted price and build the report
report = {}
for product in products:
    item, price, color, discount = product
    discounted_price = round(price * (1 - discount / 100), 2)
    
    report[item] = {
        'Price': price,
        'Available Colors': color,
        'Discounted Price': discounted_price
    }

# Print the report
print("******************************************")
print(report)
print("******************************************")