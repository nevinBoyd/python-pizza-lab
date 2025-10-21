"""
File: pizza_order_cost.py
Author: Nevin Boyd
Description: Calculates the total cost of a pizza order based on size, toppings, and delivery distance.
"""

# Step 1: Gather user inputs
size = input("Enter pizza size (small or large): ").lower()
toppings = int(input("Enter the number of toppings: "))
distance = int(input("Enter delivery distance in miles: "))

# Step 2: Determine base price
if size == "small":
    base_price = 8
elif size == "large":
    base_price = 12
else:
    print("Invalid size entered. Defaulting to small pizza.")
    base_price = 8

# Step 3: Calculate toppings cost
toppings_cost = toppings * 1

# Step 4: Calculate delivery fee
if distance <= 5:
    delivery_fee = 2
else:
    delivery_fee = 2 + (distance - 5) * 1

# Step 5: Calculate total cost
total_cost = base_price + toppings_cost + delivery_fee

# Step 6: Display final cost
print(f"\nYour total pizza order cost is: ${total_cost}")
