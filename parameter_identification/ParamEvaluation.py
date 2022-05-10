import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# global variables and paths
sample_path = os.path.expanduser('~/demonstrator_software/logs/prbs_paramident/LK1/cat')

# data set of measurements
class Measurements:
    def __init__(self, path_to_data):
        data = pd.read_csv(path_to_data, header=0, skiprows=0)    #Path to measurements
        data = data.to_numpy()

        self.tt = 0.001 * data[:, 0]           # in s
        self.tt = self.tt - self.tt[0]
        self.des_cur = 0.001 * data[:, 1]   # in A
        self.pos = 0.001 * data[:, 2]       # in m
        self.pos = self.pos - self.pos[0]

        self.dt = (np.array(self.tt[-1]) - np.array(self.tt[0]))/ self.tt.size #sample period
        self.vel = np.gradient(self.pos, self.dt)
        self.cur = 0.001 * data[:, 4]      # in A


if __name__ == '__main__':

    # calculating weighted squared error of all data sets:
    # starting with weight 1 at t = 0 and linear decay to 0.1 at t_end
    number_of_sets = 8
    error = 0
    for sample_set in range(0, number_of_sets):
        path_string = sample_path + "/sample" + str(sample_set) + ".csv"
        meas = Measurements(path_string)

    print ("quadratic model error: ", 0)

    # plotting of last set of samples for basic validation
    plt.figure(1)
    plt.plot(meas.tt, meas.pos, 'r',label="measured position")
    plt.legend()
    plt.title('Plot')
    plt.xlabel('t/s')
    plt.ylabel('x / m')

    plt.show()