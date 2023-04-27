###start of code###

#def variables
user_price = float(input("Enter the price : $"))

user_amount = float(input("Enter the amount paid : $"))


# What is the change ?? (change calculation)
user_owe = user_amount - user_price

u = float(round(user_owe, 2))

print ("Change owed : $" + str(u))


#if statement

if user_owe < 0:
    print("Insufficient funds")

#page break
print()




"""
    Calculation Program 

"""

# Using the built-in round function in Python
# Variables for Calculating Each Coin

#$100 dollars
calculate_100dollar = u//100
u = u - calculate_100dollar * 100

print("$100 dollars : " + str(calculate_100dollar))

#$50 dollar
calculate_50dollar = u//50
u = u - calculate_50dollar * 50

round(calculate_50dollar)

print("$50 dollar : " + str(calculate_50dollar))

#$20 dollar
calculate_20dollar = u//20
u = u - calculate_20dollar *20

round(calculate_20dollar)

print("$20 dollar : " + str(calculate_20dollar))

#$10 dollar
calculate_10dollar = u//10
u = u - calculate_10dollar * 10

round(calculate_10dollar)

print("$10 dollar : " + str(calculate_10dollar))

#$5 dollar
calculate_5dollar = u//5
u = u - calculate_5dollar * 5

round(calculate_5dollar)

print("$5 dollar : " + str(calculate_5dollar))

#$2 dollar
calculate_2dollar = u//2
u = u - calculate_2dollar * 2

round(calculate_2dollar)

print("$2 dollar : " + str(calculate_2dollar))

#$1 dollar
calculate_1dollar = u//1
u = u - calculate_1dollar * 1

round(calculate_1dollar)

print("$1 dollar : " + str(calculate_1dollar))


#50 cents

calculate_50cents = u//.50

round(calculate_50cents)

print("50c cents : " + str(calculate_50cents))

#25 cents

calculate_20cents = u//.20

round(calculate_20cents)

print ("20c cents : " + str(calculate_20cents))

u = u%0.20

#10 cents

calculate_10cents = u//.10

round(calculate_10cents)

print ("10c cents : " + str(calculate_10cents))

u = u%0.10

#5 cents

calculate_5cents = u//.05  

round(calculate_5cents)

print ("5c cents : " + str(calculate_5cents))

u = u%0.5

###im stuck
#dis a testin
"""
print(12.50//100)
"""
