import math

def goalLine():
    data = int(input('Give launch location: '))
    data_m = data*0.9144
    v = math.sqrt((data_m*11)/(math.sin(2*0.872665))) #launch angle is always 50
    print(v)
    p = math.exp((v+45.18761)/15.77984)
    return p, 50

def fieldGoal():
    return 'none'

def main():
    while True:
        action = input('''Action:
1. Hit goal line
2. Field goal
3. End
Choose your action: ''')
        if action == '1':
            print(f'Pressure: {goalLine()[0]} psi Angle: 50 degrees')
        elif action == '2':
            print(fieldGoal())
        elif action == '3':
            print('See ya')
            break
        else:
            print('Not a valid answer, please try again')
main()
