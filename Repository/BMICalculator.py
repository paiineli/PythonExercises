# BMI calculator exercise
print(30 * "-")

weight = float(input("Enter the patient's weight (in kg): "))
height = float(input("Enter the patient's height (in meters): "))

bmi = weight / (height * height)

print(f"The BMI is: {bmi}")

print(30 * "-")
