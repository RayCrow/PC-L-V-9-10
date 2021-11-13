import subprocess
import os
import argparse


def getScanNetwork(ip, pin, pfi):
    subprocess.Popen(['powershell',"-ExecutionPolicy","Bypass","-File", './ScanNetwork.ps1', '-ip:', ip ,'-pin:' , pin , '-pfi:' , pfi  ])

def getScanActive():
    subprocess.Popen(['powershell',"-ExecutionPolicy","Bypass","-File", './ScanActivePort.ps1'])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=' ',formatter_class=argparse.
                                RawDescriptionHelpFormatter)
    
    parser.add_argument("-ip", metavar='IP', dest="ip", required=True)
    parser.add_argument("-pin", metavar='PIN', dest="pin", required=True)
    parser.add_argument("-pfi", metavar='PFI', dest="pfi", required=True)

    ip = parser.parse_args().ip
    pin = parser.parse_args().pin
    pif = parser.parse_args().pfi

    getScanNetwork(ip,pin,pfi)

