import os
p = None
if os.uname()[0] == "Linux":
    p = True
if p:
    p = "True"
else:
    p = "False"

result = os.uname()[0] + " " + os.uname()[3][4:9] + " " + p

print(result)