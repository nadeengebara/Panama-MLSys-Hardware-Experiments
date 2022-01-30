#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import argparse 


if __name__ == "__main__":

    parser=argparse.ArgumentParser()
    parser.add_argument("--fname",nargs='+',type=str, help='specify name of data source file with extension')
    
    args=parser.parse_args()
    filenames=args.fname
    for i in range(len(filenames)):
        data = np.loadtxt(filenames[i])
        sorted_data = np.sort(data)
        yvals=np.arange(len(sorted_data))/float(len(sorted_data)-1)
        plt.plot(sorted_data,yvals)
    
    plt.xlim(8,12)
    plt.show()

