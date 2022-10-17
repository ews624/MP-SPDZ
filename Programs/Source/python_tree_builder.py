
import os
import subprocess
import time


class Node(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = []
    def add_child(self, obj):
        self.children.append(obj)

stream = os.popen('./shamir-party.x -p 0 biggest_entropy')
os.system("gnome-terminal -e 'bash -c \"cd Documents/GitHub/MP-SPDZ/;./shamir-party.x -p 1 biggest_entropy; sleep 5\" '")
os.system("gnome-terminal -e 'bash -c \"cd Documents/GitHub/MP-SPDZ/;./shamir-party.x -p 2 biggest_entropy; sleep 5\" '")



string = stream.read()

stringtoint = int(string)

test = "1"
print("The largest index is:", string)

command = "./compile.py -l unique_values "+ string

print("Command is "+command)

os.system(command)
#time.sleep(4)
stream = os.popen('./shamir-party.x -p 0 unique_values-'+string)
os.system("gnome-terminal -e 'bash -c \"cd Documents/GitHub/MP-SPDZ/;./shamir-party.x -p 1 unique_values-"+string+"; sleep 5\" '")
os.system("gnome-terminal -e 'bash -c \"cd Documents/GitHub/MP-SPDZ/;./shamir-party.x -p 2 unique_values-"+string+"; sleep 5\" '")
unique_values = stream.read()

print("The amount of unique_values is "+unique_values)

root = Node("root","")
string = string.rstrip('\n')
for i in range(0,int(unique_values)):
    root.add_child(Node(str(1)+"-"+string+"-"+str(i+1),i+1))

print("Tree Node naming convention is level-attribute Number- branch number:"+root.children[2].name)
"""
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
"""
