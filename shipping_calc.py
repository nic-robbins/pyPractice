#ground shipping
weight = 41.5
flat_charge = 20.00

if weight < 2:
  ground_cost = 1.50 * weight + flat_charge
elif (weight > 2 ) and (weight <= 6):
  ground_cost = 3.00 * weight + flat_charge
elif (weight > 6 ) and (weight <= 10):
  ground_cost = 4.00 * weight + flat_charge
else:
  ground_cost = 8.00 * weight + flat_charge

#ground premium
premium_cost = 125.00

#drone shipping
drone_weight = weight

if drone_weight < 2:
  drone_cost = float(4.50 * drone_weight)
elif (drone_weight > 2 ) and (drone_weight <= 6):
  drone_cost = float(9.00 * drone_weight)
elif (drone_weight > 6 ) and (drone_weight <= 10):
  drone_cost = float(12.00 * drone_weight)
else:
  drone_cost = float(14.25 * drone_weight)

cost_calc = [drone_cost, premium_cost, ground_cost]

print(f"Shipping with ground: ${ground_cost}")
print(f"Shipping with premium: ${premium_cost}")
print(f"Shipping with drone: ${drone_cost}")




