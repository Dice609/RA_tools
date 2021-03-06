#!/usr/bin/env python3

import sys, getopt, datetime, subprocess, os, time
from termcolor import cprint

os.chdir('/home/pi/RA_tools/RAtestmay23')

def Time_get():
    return datetime.datetime.time(datetime.datetime.now()).strftime("%H:%M:%S")


def Args(argv, var):
    Start_time = ''
    Activations = ''
    rtlPow_var = ''

    try:
          opts, Args = getopt.getopt(argv,"s:n:r:",["Start_time=","Activations","rtlPow_var"])

    except getopt.GetoptError:
          print ("raDataCollect -s start_time -n number of activations -r rtl_power command")
          sys.exit(2)

    for opt, Args in opts:
        if opt in ("-s", "--Start_time"):
            if(var) == 'S':
                return Args
        elif opt in ("-n", "--Activations"):
            if(var) == 'A':
                return Args
        elif opt in ("-r", "--rtlPow_var"):
            if(var) == 'R':
                return Args

def main():
    i = 0
    print("Will Start at:" + Args(sys.argv[1:], 'S'))

    while i < 1 :
        if str(Time_get()) == Args(sys.argv[1:], 'S'):
            print("Starting")
            while i < int(Args(sys.argv[1:], 'A')):
#               fileFFT_name = str(i) + str(Args(sys.argv[1:], 'S')) + "FFT.csv"
                fileFFT_name = "FFT" + '-' + str(i) + ".csv"
                cprint("observation" + str(i), 'green')
                process = subprocess.Popen(Args(sys.argv[1:], 'R') + " " + fileFFT_name, shell=True)
                process.wait()
                i += 1
        else:
            time.sleep(1)



if __name__ == "__main__":
    main()
    cprint("All Done", 'green')
