import random
choices = ("Have a great day", "Get Married", "Sleep", "Eat some food") 
numbers = (1,2,3,4,5,6,7,8,9,10)

luckynumber = random.choice(numbers)
fortune = random.choice(choices)

print("Your lucky number is", luckynumber, end = ' ')
print(fortune)

