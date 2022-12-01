height = input ("What is your height")
weight = input ("What is your weight")
height = float(height)
weight = float(weight)
gender = input ("what is your gender M/F")

BMI = weight/(height * height)
print ("Your BMI is", BMI)

if (gender == 'f') or (gender == 'F'):
    if BMI < 18:
        print ("You are underweight")
    elif BMI > 25:
        print ("You are overweight")
    else:
        print ("you are healthy weight")

elif gender == 'm':
    if BMI < 19:
        print ("You are underweight")
    elif BMI > 26:
        print ("You are overweight")
    else:
        print ("you are healthy weight")

else:
    print ("wrong gender selected")
 
