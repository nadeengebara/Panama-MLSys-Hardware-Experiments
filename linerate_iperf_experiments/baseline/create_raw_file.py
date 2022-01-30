#!/usr/bin/env python

import numpy as np

import argparse 


if __name__ == "__main__":

    parser=argparse.ArgumentParser()
    parser.add_argument("inputfname",nargs='+',type=str, help='specify name of data source file with extension')
      
    args=parser.parse_args()
    filename=args.inputfname[0]
    print(filename)
    file1 = open(filename,"r")    
    vals=file1.read().splitlines()
    file1.close()
    outputfile="raw_"+filename.split(".")[0]+"_gbps.txt"

    file2=open(outputfile,"w")
    for num,throughput in enumerate(vals):
        file2.write("("+str(num)+","+str(throughput)+")\r\n")
    file2.close()

