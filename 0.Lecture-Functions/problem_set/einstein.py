# einstein.py - Einstein's Mass-Energy Equivalence

# Speed of light in m/s
speed_of_light = 3 * 10**8

# Prompt the user for mass in kilograms using the `input()` function.
mass = int(input("Enter mass in kg: "))

# Calculate energy in joules using Einstein's mass-energy equivalence equation: E = m * c^2.
joules = mass * speed_of_light**2

# Print the calculated energy in joules using an f-string.
print(f"Energy in Joules: {joules} J")



# In this section, the program calculates energy using Einstein's mass-energy equivalence equation (E = m * c^2).
# The speed of light is defined as a constant. The input() function is used to prompt the user for the mass in
# kilograms, which is stored in the variable mass. The calculated energy in joules is printed using an f-string.