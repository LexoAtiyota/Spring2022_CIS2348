import math
wall_height = int(input("Enter wall height (feet):\n"))
wall_width = int(input("Enter wall width (feet):\n"))
wall_area = wall_width * wall_height
print("Wall area:", wall_area, 'square feet')

one_gallon = 1/350
print("Paint needed:",'{:.2f}'.format(one_gallon*wall_area), 'gallons')
paint_needed = float("{:.2f}".format(one_gallon * wall_area))
print("Cans needed:", math.ceil(paint_needed), 'can(s)\n')

color_group = {'red': 35,
               'blue': 75,
               'green': 23}
color_choice = input("Choose a color to paint the wall:\n")
print('Cost of purchasing',color_choice,'paint:', '$'+ str(color_group[color_choice]))
