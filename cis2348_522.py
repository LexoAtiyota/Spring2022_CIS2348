output_menu = """Davy's auto shop services
Oil change -- $35
Tire rotation -- $19
Car wash -- $7
Car wax -- $12
"""
automobile_service = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12}
print(output_menu)

shop_service1 = input('Select first service:\n')
shop_service2 = input("Select second service:\n")
print()

print("Davy's auto shop invoice")
print()
print('Service 1:', shop_service1 + ',', '$' + str(automobile_service[shop_service1]))
print('Service 2:', shop_service2 + ',', '$' + str(automobile_service[shop_service2]))
print()
print('Total:\t$',((automobile_service[shop_service1])+automobile_service[shop_service2]))

if shop_service1 == '-':
    print("Service 1: No service")
else:
    print('Service 1:', shop_service1 + ',', '$' + str(automobile_service[shop_service1]))
if shop_service2 =='-':
    print("Service 2: No service")
else:
    print('Service 2:', shop_service2 + ',', '$' + str(automobile_service[shop_service2]))