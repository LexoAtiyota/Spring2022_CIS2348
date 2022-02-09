amount_of_lemon_juice = float(input("Enter amount of lemon juice (in cups):\n"))
amount_of_water = float(input("Enter amount of water (in cups):\n"))
agave_nectar = float(input("Enter amount of agave nectar (in cups):\n"))
#Converted all of these values since they are float (decimal values)
num_of_servings = float(input("How many servings does this make?\n"))
print()

print("Lemonade ingredients - yields", '{:.2f}'.format(num_of_servings), 'servings')
print('{:.2f}'.format(amount_of_lemon_juice), 'cup(s) lemon juice')#Using this format to get two decimal points
print('{:.2f}'.format(amount_of_water), 'cup(s) water')
print('{:.2f}'.format(agave_nectar), 'cup(s) agave nectar\n')


second_servings = float(input("How many servings would you like to make?\n"))
amount_of_lemon_juice = amount_of_lemon_juice/num_of_servings * second_servings
amount_of_water = amount_of_water/num_of_servings * second_servings
agave_nectar = agave_nectar/num_of_servings * second_servings
print()

num_of_servings = second_servings
print("Lemonade ingredients - yields",'{:.2f}'.format(num_of_servings), 'servings')
print('{:.2f}'.format(amount_of_lemon_juice), 'cup(s) lemon juice')#Using this format to get two decimal points
print('{:.2f}'.format(amount_of_water), 'cup(s) water')
print('{:.2f}'.format(agave_nectar), 'cup(s) agave nectar\n')


print('Lemonade ingredients - yields','{:.2f}'.format(num_of_servings), 'servings')
print('{:.2f}'.format(amount_of_lemon_juice/16), 'gallon(s) lemon juice')
print('{:.2f}'.format(amount_of_water/16), 'gallon(s) water')
print('{:.2f}'.format(agave_nectar/16), 'gallon(s) agave nectar')

