# Furniture.py - This program calculates profits and sales prices for a furniture company.

item_name = ("TV Stand")
retail_price = float(325.00)
wholesale_price = 200.00

# Calculate the profit
profit = retail_price - wholesale_price

# Calculate the sale price (25% off)
sale_price = retail_price * 0.75

# Calculate the profit when sold at the sale price
sale_profit = sale_price - wholesale_price

print("item_name: " + item_name)
print("retail_price: $" + str(retail_price))
print("wholesale_price: $" + str(wholesale_price))
print("profit: $" + str(profit))
print("sale_price: $" + str(sale_price))
print("sale_profit: $" + str(sale_profit))