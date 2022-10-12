#Python caller


import os
import subprocess


print('Hello')

#stream = os.popen('./emulate.x python_caller')
stream = os.popen('./shamir-party.x -p 0 python_caller')
os.system("gnome-terminal -e 'bash -c \"cd Documents/GitHub/MP-SPDZ/;./shamir-party.x -p 1 python_caller; sleep 5\" '")
os.system("gnome-terminal -e 'bash -c \"cd Documents/GitHub/MP-SPDZ/;./shamir-party.x -p 2 python_caller; sleep 5\" '")



string = stream.read()
test = "1"
print("The string is:", string)
if test in string:
    print('All items in the array are the same')
    stream = os.popen('./emulate.x Same-called')
    string = stream.read()
    print("The string is:", string)
else:
    print("There are different values in the array")
    stream = os.popen('./emulate.x Unique-called')
    string = stream.read()
    print("The string is:", string)
