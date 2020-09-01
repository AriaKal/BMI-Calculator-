# Get your BMI and its corresponding health status

import math

GREETING = "Welcome to the BMI-Ometer!"
GET_HEIGHT = "Please enter your height in centimeters (cm)."
GET_WEIGHT = "Please enter your weight in killograms (kg)."

# Greet
print("\n"+GREETING)

# Colelct height data
print(GET_HEIGHT)
height = input()

# Colelct weight data
print(GET_WEIGHT)
weight = input()
 
# Calculate BMI
height_squared = (float(height) / 100) ** 2
BMI = float(weight) / height_squared

# Deduce Health Status
health_status = None
if(BMI < 18.5):
	health_status = "Underweight"
elif (BMI > 18.5 and BMI < 25):
	health_status = "Healthy"
else:
	if (BMI > 25 and BMI < 30):
		health_status = "Overweight"
	else:
		health_status = "Obese"

# Print results		
print(f"Your BMI is {str(round(BMI,2))} - {health_status}\n")