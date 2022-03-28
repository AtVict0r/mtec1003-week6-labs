print("BMI: Body Mass Index Calculator")

weight = float(input("Enter your weight (in pounds): "))
print("You entered " + str(weight) + " pounds")

height = float(input("Enter your height (in inches): "))
print("You entered " + str(height) + " inches")

bmi = (703 * weight) / (height ** 2)
print("Your body mass index (BMI) is " + str(bmi))