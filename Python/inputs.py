my_first = input('first? ')
other_door_first = input('other door first? ')

my_coding_month = int(input('how many month coding?'))
other_door_coding_month = int(input('how many month your next door coding?'))

totla_month = my_coding_month + other_door_coding_month

print("your name is " + my_first + ' and has been coding for ' + str(my_coding_month) + '\n')
print("next door name is " + other_door_first + ' and has been coding for ' + str(other_door_coding_month) + '\n')

print("combined month: " + str(totla_month))
