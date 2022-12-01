size_options = ["small","medium","large","extra large"]
toppings_options = ["pineapple", "mushroom","exta cheese", "sausage", "onion", "black olives","green pepper", "sarlic"]
crust_options = ["thin Crust", "deep Pan", "stuffed Crust","thin", "deep", "stuffed"]
option_toppings_confirm=("yes","no")



size = []
crust = []
toppingslist = []

size = input ("What size pizza would you like to order.Small,Medium,Large or Extra Large.").lower()

while size not in size_options:
    print("This is not a valid option")
    size = input ("What size pizza would you like to order.Small,Medium,Large or Extra Large.").lower()

crust= input("What pizza crust would you like to order.Thin,Deep Pan or stuffed crust.").lower()
while crust not in crust_options:
    print("This is not a valid option")
    crust= input("What pizza crust would you like to order.Thin,Deep Pan or stuffed crust.").lower()
    
no_toppings = int(input("How many toppings would you like? Maximum 5"))
while no_toppings not in range(1, 5):
    print("This is not a valid number of toppings")
    no_toppings = int(input("How many toppings would you like?")) 
for i in range(no_toppings):
    toppings = input ("What Toppings would you like").lower()
    toppingslist.append(toppings)
    while toppings not in toppings_options:
        print("This is not a valid number of toppings")
        toppings = input ("What Toppings would you like").lower()
        toppingslist.append(toppings)


print("Your toppings are", toppingslist)
option_toppings_confirm=("yes","no")
toppings_confirm = input("Is this correct, Yes or No").lower()

while toppings_confirm not in option_toppings_confirm:
    print("This is not a option")
    toppings_confirm = input("Is this correct, Yes or No").lower()

while toppings_confirm == "no":
    del toppingslist
    no_toppings = int(input("How many toppings would you like?"))
    while no_toppings not in range(1, 5):
        print("This is not a valid number of toppings")
        no_toppings = int(input("How many toppings would you like?")) 

    for i in range(no_toppings):
        toppings = input ("What Toppings would you like").lower()
        toppingslist=()
        toppingslist.append(toppings)
        print("Your toppings are", toppingslist)
    option_toppings_confirm=("yes","no")
    toppings_confirm = input("Is this correct, Yes or No").lower()



    
    
    while toppings not in toppings_options:
        print("This is not a valid option")
        toppings = input ("What Toppings would you like").lower()

    
    
print("You have ordered a", size, end=' ')
print("Pizza with", crust, "Crust", end=' ')
print("With toppings", toppingslist)



