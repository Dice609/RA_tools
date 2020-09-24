#!usr/bin/python3

import sys, getopt, datetime, subprocess


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

# I dont care what anyone says, there must be a better way too do this...

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
        #start when when S == Time_get
        if str(Time_get()) == Args(sys.argv[1:], 'S'):
            print("Started")
            #loop N times
            while i < int(Args(sys.argv[1:], 'A')):
                print("loop")
                #Command too be run
                subprocess.Popen(Args(sys.argv[1:], 'R'), shell=True)
                i += 1



if __name__ == "__main__":
    main()
    print("All Done")
