from scipy.integrate import odeint
from math import *
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse


a = 0 
b = 1
# ryuya is '17236014'
# alpha = 24
# beta = 1008

def derivative(x, t):
    global a, b
    b = int(b)
    dx = [ x[1], -b * x[0] - a * x[1] + 1.0 ]
    return dx

def calc_alpha_beta(n):
    global a, b
    for i in n[0]:
        a = a + int(i)
        if (i == '0'):
            pass
        else:
            b = b * int(i)
    print(a, b)
    b = str(b)[-3:]
    print(a, b)

def run(n):
    calc_alpha_beta(n)
    time = np.linspace(0.0, 50.0, 10000)
    x_init = [0.0, 0.0]
    x = odeint(derivative, x_init, time)
    
    plt.figure()
    plt.plot(time, x[:,0])
    plt.savefig('figure.png')
    # plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', nargs=1,type=str, help='Please input your school number.', required=True)
    args = parser.parse_args()
    run(args.number)
