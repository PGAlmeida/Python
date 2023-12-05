'''
import subprocess

meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

data = meta_data.decode('utf-8', errors='backslashreplace')

data = data.split('\n')

profiles = []

for i in data:
    if "All User Profile" in i:
        i = i.split(':')

        i = i[1]

        i = i[1:-1]

        profiles.append(i)

print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("----------------------------------------------")

for i in profiles:
    try:
        results  = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key = clear'])

        results = results.decode('utf-8', errors='backslashreplace')
        results = results.split('\n')

        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

        try:
            print("{:<30}| {:<}".format(i, results[0]))

        except IndexError:
            print("{:<30}| {:<}".format(i, " "))

    except subprocess.CalledProcessError:
        print("Encoding Error Occured")



import os
from random import randint

pas = input('digite sua senha: ')

keys = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

pwg = ""

while(pwg!=pas):
    pwg=""
    for i in range(len(pas)):
        guessPass = keys[randint(0,4)]
        pwg = str(guessPass)+str(pwg)
        print(pwg)
        print("Attacking... please wait!")
        os.system("cls")

    print(f"The pass is: {pwg}")
    '''

