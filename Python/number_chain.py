
prevNum = 0
run = 'y'
while run == 'y':
    num = int(input('how many? '))
    if prevNum > num:
        print('\n'.join([ str(i) for i in reversed(range(num, prevNum))] ))
    else:
        print('\n'.join([ str(i) for i in reversed(range(prevNum, num))] ))
    run = input('run?')
    prevNum = num