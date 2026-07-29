try :
    hours = float(input('hours: '))
    rate = float(input('rate: '))
except:
    print('Error, please enter numeric')
    quit()
if  hours < 0 or rate < 0:
    print('Error, Enter a positive number')
    quit()
elif hours > 40:
    pay = (40 * rate) + (hours - 40) * (rate * 1.5)
    print(f'Pay: {pay:.2f}')
else:
    regular_pay = hours * rate
    print(f'Pay: {regular_pay:.2f}')
