
try:
    Score1 = float(input('Enter Score 1: '))
    Score2 = float(input('Enter Score 2: '))
    Score3 = float(input('Enter Score 3: '))
except ValueError:
    Score1 < 0 or Score2 < 0 or Score3 < 0 or Score1 > 100 or Score2 > 100 or Score3 > 100:
    Average = (Score1 + Score2 + Score3) / 3
    print('Error, please enter a score between 0 and 100')
    quit()  
if Average >= 90:
    print('A')
elif Average >= 80:
    print('B')
elif Average >= 70:
    print('C')
elif Average >= 60:
    print('D')
else: 
    print('F')