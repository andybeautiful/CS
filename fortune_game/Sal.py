weight = 4.8

if weight <= 2:
    cost_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
    cost_ground = weight * 3 + 20
elif weight > 6 and weight <= 10:
    cost_ground = weight * 4 + 20
else:
    cost_ground = weight * 4.75 + 20

print(cost_ground)


cost_ground_premium = 125.00
print("Ground Shipping Premium $", cost_ground_premium)
  
  # Drone Shipping

weight = 1

if weight <= 2:
    cost_ground = weight * 4.5 + 0.00
elif weight > 2 and weight <= 6:
    cost_ground = weight * 9 + 0.00
elif weight > 6 and weight <= 10:
    cost_ground = weight * 12 + 0.00
else:
    cost_ground = weight * 10 + 0.00

print(cost_ground)
