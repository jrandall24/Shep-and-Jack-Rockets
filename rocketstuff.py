import math

def goalLine(): # g=11
    data = int(input('Give launch location: '))
    data_m = data*0.9144
    v = math.sqrt((data_m*11)/(math.sin(2*0.872665))) #launch angle is always 50
    p = math.exp((v+45.18761)/15.77984)
    return p, 50

def fieldGoal(): # 20 ft = 6.069 m
    data = input('Give launch angle and launch location: ').split()
    angle = int(data[0])*(math.pi/180)
    x = (int(data[1])*0.9144)+9.144
    try:
        v = math.sqrt((11*(x**2))/((2*(math.cos(angle)**2))*((x*math.tan(angle))-6.069)))
        p = math.exp((v+45.18761)/15.77984)
        return p
    except:
        return 'unavailable'

def main():
    while True:
        action = input('''Actions:
1. Hit goal line
2. Field goal
3. End
Choose your action: ''')
        if action == '1':
            print(f'Pressure: {goalLine()[0]} psi Angle: 50 degrees')
        elif action == '2':
            print(f'Pressure: {fieldGoal()} psi')
        elif action == '3':
            print('See ya')
            break
        else:
            print('Not a valid answer, please try again')
main()
