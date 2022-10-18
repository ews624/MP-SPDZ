
import os
import subprocess
import time


shapeTuple = ("None","Triangle","Square")

class Node(object):
    def __init__(self, name, value,shape):
        self.name = name
        self.value = value
        self.children = []
        self.shape = ()
    def add_child(self, obj):
        self.children.append(obj)

def preorder(Node):
    if Node:
        print(Node.name)
        if Node.children:
            preorder(Node.children[0])
            preorder(Node.children[1])
            preorder(Node.children[2])


stream = os.popen('./shamir-party.x -p 0 biggest_entropy')
os.system("gnome-terminal -e 'bash -c \"cd Documents/GitHub/MP-SPDZ/;./shamir-party.x -p 1 biggest_entropy; \" '")
os.system("gnome-terminal -e 'bash -c \"cd Documents/GitHub/MP-SPDZ/;./shamir-party.x -p 2 biggest_entropy; \" '")



string = stream.read()

stringtoint = int(string)

test = "1"
print("The largest index is:", string)

command = "./compile.py -l unique_values "+ string

print("Command is "+command)

os.system(command)
#time.sleep(4)
stream = os.popen('./shamir-party.x -p 0 unique_values-'+string)
os.system("gnome-terminal -e 'bash -c \"cd Documents/GitHub/MP-SPDZ/;./shamir-party.x -p 1 unique_values-"+string+"; sleep 4\" '")
os.system("gnome-terminal -e 'bash -c \"cd Documents/GitHub/MP-SPDZ/;./shamir-party.x -p 2 unique_values-"+string+"; sleep 4\" '")
unique_values = stream.read()

print("The amount of unique_values is "+unique_values)

root = Node("root","",shapeTuple[0])
string = string.rstrip('\n')
for i in range(0,int(unique_values)):
    root.add_child(Node(str(1)+"-"+string+"-"+str(i+1)+"-"+shapeTuple[0],i+1,shapeTuple[0]))

print("Tree Node naming convention is level-attribute Number- branch number-Shape:"+root.children[2].name)

preorder(root)

##Check Entropy
#if 0 then dont add Node
#else add nodes

for i in range(1,int(unique_values)+1):

    string = str(i)
    command = "./compile.py -l unique_values "+ string

    print("Command is "+command)

    os.system(command)
    stream = os.popen('./shamir-party.x -p 0 Node_entropy-'+string)
    os.system("gnome-terminal -e 'bash -c \"cd Documents/GitHub/MP-SPDZ/;./shamir-party.x -p 1 Node_entropy-"+string+"; sleep 2\" '")
    os.system("gnome-terminal -e 'bash -c \"cd Documents/GitHub/MP-SPDZ/;./shamir-party.x -p 2 Node_entropy-"+string+"; sleep 2\" '")
    sameShapes =stream.read()
    sameShapes = sameShapes.rstrip('\n')
    print("If it is 0 that means there is no entropy: "+sameShapes)

    if int(sameShapes) == 0:
        print("ITS ZERO \n\n\n\n\n")
        #get Shape once entropy is zero
    #else: continue the tree
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
