#Python caller


import os
import subprocess


print('Hello')

stream = os.popen('./emulate.x python_caller')
string = stream.read()
test = "1"
print("The string is:", string)
if test in string:
    print('Test passed')

else:
    print("test did not pass")
    
