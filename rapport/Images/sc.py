import os

cmd = 'find . -iname "*noise*.png" -type f'
lines = os.popen(cmd).readlines()

for line in lines:
    line = line.strip()
    a,b = line.split("noise_0.")
    newfile = a + "noise_0_" + b
    mv = "mv " + line + " " + newfile
    print(mv)
    os.popen(mv).readlines()
