import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

global g, m_convert, theta
g = 11
m_convert = 0.9144
theta = 0.785398

def goalLine(): #g = 11
    while True:
        try:
            data = float(input('Give launch location (yd line): '))
            data_m = data*m_convert
            #print(data_m)
            v = math.sqrt((data_m*g)/(math.sin(2*theta))) #launch angle is always 45 (45 degrees = 0.785398 radians)
            #print(v)
            p = math.exp((v+45.18761)/15.77984)
            animate_launch(v, theta, data_m, 0, p)
            break
        except:
            print('Incorrect input')
            break

def fieldGoal(): #20 ft = 6.069 m
    while True:
        try:
            data = input('Give launch angle and launch location (yd line): ').split()
            angle = float(data[0])*(math.pi/180)
            x = (float(data[1])*m_convert)+9.144
            #print(x)
            try:
                v = math.sqrt((g*(x**2))/((2*(math.cos(angle)**2))*((x*math.tan(angle))-6.069)))
                #print(v)
                p = math.exp((v+45.18761)/15.77984)
                animate_launch(v, angle, x, 6.069, p)
                break
            except:
                print('Impossible for sufficient height to be obtained given the inputted angle and location')
                break
        except:
            print('Incorrect input')
            break

def animate_launch(v0, angle_rad, target_x, target_y, p):
    g = 11 
    #total flight time
    t_total = target_x / (v0 * math.cos(angle_rad))
    t_points = np.linspace(0, t_total, 100)
    #path coordinates
    x_path = v0 * np.cos(angle_rad) * t_points
    y_path = v0 * np.sin(angle_rad) * t_points - 0.5 * g * t_points**2

    fig, ax = plt.subplots()
    line, = ax.plot([], [], 'black', lw=2)  # trajectory
    rocket, = ax.plot([], [], 'ro')         # moving rocket 
    x_display = ax.text(0.02, 0.95, '', transform=ax.transAxes, 
                        fontsize=10, fontweight='bold',
                        verticalalignment='top',
                        bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
    #visuals
    ax.axhline(target_y, color='r', linestyle='--', label='Goal Height')
    ax.set_xlim(0, target_x + 5)
    ax.set_ylim(0, max(y_path) + 2)
    ax.set_title(f"Rocket Trajectory\nRequired Pressure: {p:.2f} PSI", 
                 fontsize=12, color='darkblue')
    ax.legend()

    def update(frame):
        line.set_data(x_path[:frame], y_path[:frame])
        rocket.set_data([x_path[frame]], [y_path[frame]])
        current_x = x_path[frame]
        x_display.set_text(f"{current_x:.2f} m")
        return line, rocket, x_display
    ani = FuncAnimation(fig, update, frames=len(t_points), interval=20, repeat=False)
    plt.show()

def main():
    while True:
        action = input('''Actions:
1. Hit goal line
2. Field goal
3. End
Choose your action: ''')
        if action == '1':
            goalLine()
        elif action == '2':
            fieldGoal()
        elif action == '3':
            print('See ya')
            break
        else:
            print('Not a valid answer, please try again')
main()
