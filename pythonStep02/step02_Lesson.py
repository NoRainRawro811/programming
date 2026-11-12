price = 8.99
print(int(price))
print(round(8.8275, 2))

# He backspaced everything 

# "Named constants"
SALES_TAX_RATE = 0.0675 
SHIPPING_COST = 4.99 

# "Processing"
order_amount = 40.00
tax = order_amount * SALES_TAX_RATE 
total = order_amount + tax + SHIPPING_COST 
print(round(total, 2))
print(f"total: ${total}")
print(f"total: ${total:.2f}")

# Backspaced again. 
print("")
player = "Jacob"
points = 25 
cost = 3.5

#"output"
print(f"{player} scored {points} points.")
print(f"cost: ${cost}")


# Backspaced again.
print("")
# Name: Aurora Tackett
# Date: 2026/11/12 
# Program: Carpet Cost Example
# Description: Calculate cost to carpet room, plus a fee. 

# Named constant for the install fee
INSTALL_FEE = 25.00

# Input: Room owner, cost per square foot, and room size
owner = input("Owner: ")
cost_per_foot = float(input("Cost per square foot: "))
square_feet = int(input("Square feet: "))

# Processing material cost and the total amount
material_cost = cost_per_foot * square_feet
total_cost = material_cost + INSTALL_FEE

# Output: A small report, format $ to 2 decimal places
print(f"--- Estimate for {owner} ---")
print(f"Material:   ${material_cost:.2f}")
print(f"Install:    ${INSTALL_FEE:.2f}")
print(f"Total:      ${total_cost:.2f}")

