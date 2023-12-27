print("\nBMI CALCULATOR FOR ALF\n")

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
      bmi_calcu = "\nHEIGHT: %.2lf - WEIGHT: %.2lf\nBMI: %.2lf - NUTRITIONAL STATUS: underweight" % (height, weight, bmi)
      print(bmi_calcu)
elif bmi >= 18.5 and bmi <= 24.9: 
      bmi_calcu = "\nHEIGHT: %.2lf - WEIGHT: %.2lf\nBMI: %.2lf - NUTRITIONAL STATUS: normal weight" % (height, weight, bmi)
      print(bmi_calcu)
elif bmi >= 25.9 and bmi <= 29.9:
      bmi_calcu = "\nHEIGHT: %.2lf - WEIGHT: %.2lf\nBMI: %.2lf - NUTRITIONAL STATUS: overweight" % (height, weight, bmi)
      print(bmi_calcu)
elif bmi > 30.0:
      bmi_calcu = "\nHEIGHT: %.2lf - WEIGHT: %.2lf\nBMI: %.2lf - NUTRITIONAL STATUS: obesity" % (height, weight, bmi)
      print(bmi_calcu)
else:
      print("Invalid input. Try again.")