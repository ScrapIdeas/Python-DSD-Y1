weight_kg = 0
height_m = 0
bmi = 0

weight_kg = float(input("Put in your weight."))
weight_kg = weight_kg * 100
height_m = float(input("Put in your height."))
bmi = weight_kg / (height_m **2)
round(bmi,1)

if(bmi < 18.5):
    print("You're underweight.")
elif(18.5 <= bmi <= 24.9):
    print("You're a normal weight.")
elif(25 <= bmi <= 29.9):
    print("You're slightly overweight.")
elif(30 <= bmi <= 34.9):
    print("You're obese.")
elif(35 <= bmi >= 35):
    print("You're extremely obese.")