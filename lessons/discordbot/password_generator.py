import random

pwchar = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
pwlength = int(input("Please enter your prefered password length:"))

pw = ""

for i in range(pwlength):
    pw += random.choice(pwchar)

print(pw)