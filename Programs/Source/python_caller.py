#Python caller


import os
import subprocess


print('Hello')

stream = os.popen('./emulate.x python_caller')
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
