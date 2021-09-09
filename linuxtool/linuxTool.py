import sys 

import os

if os.getuid() != 0:

    print("Sorry. This script requires sudo privledges")

    sys.exit()

os.system("sudo apt install sysvbanner")

print("  ")

print("  ")

print("  ")

print("  ")

print("  ")

print("  ")

print("  ")



os.system("banner Fareeq")

print('are you sure you want to install more than 2.5 GB on your system \n " press anything if you want to continue or press ctrl+c to cancel "')

raw_input(">")



f=open(os.path.join(sys.path[0], "apts.txt"), "r") 

str1=f.read()

os.system(str1)

print(" good bye ...")

sys.exit()















