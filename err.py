#first test
try:
    hours_worked = float(input("Enter Hours: "))
    hourly_rate = float(input("Enter Rate: "))
except ValueError:
    print("Error, please enter a numeric input")
    quit()
if hours_worked > 40:
    overtime_pay = (40 * hourly_rate) + (hours_worked - 40) * (hourly_rate * 1.5)
    print("Pay:", overtime_pay)
elif hours_worked < 0 or hourly_rate < 0:
    print("Error, please enter a positive number")
    quit()
else:
    regular_pay = hours_worked * hourly_rate
    print("Pay:", regular_pay)
   
        
