import random
a=int(input("Length of password:-"))
b='abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
c=""
for i in range(a):
    c=c+random.choice(b)
print(c)